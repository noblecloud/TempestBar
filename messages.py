import logging
import pprint
from datetime import datetime, timedelta

import pytz

from constants import classAtlas, summaryAtlas, dewpointCalc, airDensityCalc
from WeatherUnits.defaults.WeatherFlow import Heat, Wind
from WeatherUnits.length import Length
from WeatherUnits.others import Direction, Humidity, Lux, RadiantFlux, Volts
from WeatherUnits.pressure import Pressure
from WeatherUnits.time import Minute, Second


class DataMessage(dict):

	def __init__(self):
		super().__init__()

	@property
	def data(self) -> dict:
		return self['data']

	@property
	def time(self) -> datetime:
		return self.data['time']

	@property
	def reportInterval(self) -> Minute:
		return self.data['reportInterval']

	@property
	def formatMessage(self) -> str:
		return pprint.pformat(self)


class Observation(DataMessage):
	messAtlas = {'serial_number': 'serial',
	             'hub_sn':        'hub',
	             'deviceID':      'device_id'}

	atlas = ['time']

	def __init__(self, udpData):
		udpData = self.translate(udpData, self.messAtlas)
		if 'data' in udpData:
			udpData['data'] = self.convert(udpData['data'], self.atlas)
			udpData['time'] = datetime.fromtimestamp(int(udpData['data'].pop('time')), pytz.timezone('America/New_York'))
		self.update(udpData)
		super(Observation, self).__init__()

	@staticmethod
	def translate(udpData: dict, atlas: dict[str:str]):
		translated = {}
		for key in udpData:
			if key in atlas:
				newKey = atlas[key]
				translated[newKey] = udpData[key]
			else:
				translated[key] = udpData[key]
		return translated

	# return {key: udpData[value] for key, value in atlas.items()}
	# translated = {}
	# for native, foreign in atlas.items():
	# 	try:
	# 		translated.update({native: udpData[foreign]})
	# 	except KeyError:
	# 		logging.error('Unable to translate: {}'.format(native))
	# return translated

	@staticmethod
	def convert(data, atlas):
		converted = {}
		if isinstance(data, list):
			if len(data) == 1:
				data = data[0]
			for key, value in zip(atlas, data):
				try:
					converted[key] = classAtlas[key](value).localized
				except AttributeError:
					converted[key] = classAtlas[key](value)
		elif isinstance(data, dict):
			for key, value in data.items():
				try:
					converted[key] = classAtlas[key](value).localized
				except AttributeError:
					converted[key] = classAtlas[key](value)
		return converted

	def __setitem__(self, *args):
		logging.error('UDP Messages are immutable')


class StatusMessage(dict):
	atlas = {'time':     'timestamp',
	         'type':     'type',
	         'serial':   'serial_number',
	         'uptime':   'uptime',
	         'firmware': 'firmware_revision',
	         'rssi':     'rssi',
	         }

	def __init__(self, udpData):
		data = {key: udpData[value] for key, value in self.atlas.items()}
		super(StatusMessage, self).__init__(data)

	def __setitem__(self, *args):
		logging.error('UDP Messages are immutable')

	@property
	def uptime(self):
		value = timedelta(seconds=self['uptime'])
		if value.days > 0:
			return "{} days".format(value.days)
		if value.days > 30:
			return "{:2.1f} months".format(value.days / 30.5)
		elif value.min // 60 > 0:
			return "{:2.1f} hours".format(value.min / 60)
		elif value.min > 0:
			return "{} hours".format(value.min)
		else:
			return "{} seconds".format(value.seconds)

	@property
	def firmware(self):
		return "v{}".format(self['firmware'])

	@property
	def serial(self):
		return "{}".format(self['serial'])


class DeviceStatusMessage(StatusMessage):
	atlas = {**StatusMessage.atlas,
	         'serialHub':    'hub_sn',
	         'battery':      'voltage',
	         'rssiHub':      'hub_rssi',
	         'sensorStatus': 'sensor_status',
	         'debug':        'debug'}

	deviceStatus = {0: 'All OK', 1: 'Lightning failed'}

	def __init__(self, udpData):
		super(DeviceStatusMessage, self).__init__(udpData)

	@property
	def serialHub(self):
		return "{}".format(self['serialHub'])

	@property
	def rssi(self):
		return str(self['rssi'])

	@property
	def battery(self) -> Volts:
		return Volts(self['battery'])

	@property
	def rssiHub(self):
		return str(self['rssiHub'])

	@property
	def sensorStatus(self):
		return SensorStatus(self['sensorStatus'])


class SensorStatus:
	failed = []
	masks = {
			0b000000001: 'Lightning',
			0b000000010: 'LightningNoise',
			0b000000100: 'LightningDisturber',
			0b000001000: 'Pressure',
			0b000010000: 'Temperature',
			0b000100000: 'Humidity',
			0b001000000: 'Wind',
			0b010000000: 'Precipitation',
			0b100000000: 'Light/UV'
	}

	def __init__(self, value: int):
		for mask in self.masks:
			if mask & value:
				self.failed.append(self.masks[mask])

	def __str__(self):
		failures = len(self.failed)
		if not failures:
			string = 'All OK'
		elif failures == 1:
			string = '{}: Failed'.format(self.failed[0])
		elif failures == 2:
			string = '{}: Failed\n{}: Failed\n'.format(self.failed[0], self.failed[1])
		else:
			string = 'Multiple Failures'
		return string

	def __repr__(self) -> str:
		return str(self)


class HubStatusMessage(StatusMessage):
	def __init__(self, udpData):
		super(HubStatusMessage, self).__init__(udpData)


class RainStartMessage(Observation):

	def __init__(self, udpData):
		self.messAtlas['data'] = 'evt'
		super().__init__(udpData)

	@staticmethod
	def print():
		print('Rain event started')


class WindMessage(Observation):
	atlas = [*Observation.atlas, 'speed', 'direction']

	def __init__(self, udpData):
		self.messAtlas['ob'] = 'data'

		super(WindMessage, self).__init__(udpData)

	@property
	def speed(self) -> Wind:
		return self.data['speed']

	@property
	def direction(self) -> Direction:
		return self.data['direction']

	@property
	def messsage(self):
		return 'Wind recorded {}km/h at {} ({}º)'.format(self.speed, self.direction.cardinal, self.direction)


class LightMessage(Observation):
	"""
	I haven't quite figured out what this message contains.
	I am confident the item at index 2 is irradiance, but the
	item a index 1 alludes me.  It could be illuminance, but I
	can not figure out what the unit is.
	"""

	atlas = [*Observation.atlas, 'illuminance', 'irradiance', 'zero', 'zero']

	def __init__(self, udpData):
		self.messAtlas['data'] = 'ob'
		super(LightMessage, self).__init__(udpData)
		delattr(self, 'atlas')


class _Air(DataMessage):

	@property
	def pressure(self) -> Pressure:
		return self.data['pressure']

	@property
	def temperature(self) -> Heat:
		return self.data['temperature']

	@property
	def humidity(self) -> Humidity:
		return self.data['humidity']

	@property
	def strikeDistance(self) -> Length:
		return self.data['strikeDistance']

	@property
	def strikes(self) -> int:
		return self.data['strikes']


class AirMessage(Observation, _Air):
	atlas = [*Observation.atlas, 'pressure', 'temperature', 'humidity', 'lightning',
	         'lightningDistance', 'battery', 'reportInterval']

	def __init__(self, udpData):
		self.messAtlas['obs'] = 'data'
		super(AirMessage, self).__init__(udpData)


class _Sky(DataMessage):
	@property
	def uvi(self) -> int:
		return self.data['uvi']

	@property
	def accumulation(self) -> Length:
		return self.data['accumulation']

	@property
	def lullSpeed(self) -> Wind:
		return self.data['lullSpeed']

	@property
	def windSpeed(self) -> Wind:
		return self.data['windSpeed']

	@property
	def wind(self) -> Wind:
		return self.data['windSpeed']

	@property
	def gustSpeed(self) -> Wind:
		return self.data['gustSpeed']

	@property
	def windDirection(self) -> Direction:
		return self.data['windDirection']

	@property
	def battery(self) -> Volts:
		return self.data['battery']

	@property
	def reportInterval(self) -> Minute:
		return self.data['reportInterval']

	@property
	def irradiance(self) -> RadiantFlux:
		return self.data['irradiance']

	@property
	def illuminance(self) -> Lux:
		return self.data['illuminance']

	@property
	def accumulationDay(self) -> Length:
		return self.data['accumulationDay']

	@property
	def precipitationType(self) -> int:
		return self.data['precipitationType']

	@property
	def windSampleInterval(self) -> Second:
		return self.data['windSampleInterval']


class SkyMessage(Observation, _Sky):
	atlas = [*Observation.atlas, 'illuminance', 'uvi', 'accumulation', 'lullSpeed', 'windSpeed',
	         'gustSpeed', 'windDirection', 'battery', 'reportInterval', 'irradiance',
	         'accumulationDay', 'precipitationType', 'windSampleInterval']

	def __init__(self, udpData):
		self.messAtlas['obs'] = 'data'
		super(SkyMessage, self).__init__(udpData)

		if len(udpData['data'][0] == 16):
			self.atlas += ['dailyAccumulationRainCheck', 'localDailyAccumulationRainCheck', 'rainCheck']


class TempestMessage(Observation, _Sky, _Air):
	atlas = [*Observation.atlas, 'lullSpeed', 'windSpeed', 'gustSpeed', 'windDirection',
	         'windSampleInterval', 'pressure', 'temperature', 'humidity',
	         'illuminance', 'uvi', 'irradiance', 'accumulation',
	         'precipitationType', 'strikeDistance', 'strikes',
	         'battery', 'reportInterval']

	def __init__(self, udpData):
		self.messAtlas['obs'] = 'data'
		super(TempestMessage, self).__init__(udpData)
		if len(self.data) == 21:
			self.atlas += ['dailyAccumulationRaw', 'dailyAccumulationRainCheck',
			               'localDailyAccumulationRainCheck', 'rainCheck']

		if 'summary' in self:
			summary = self.translate(self['summary'], summaryAtlas)
			summary = self.convert(summary, classAtlas)
			self.data.update(summary)

		if 'rainCheck' in self.data:
			# Always assume rainCheck is on unless specified as false
			self.data['rainCheck'] = False if self.data['rainCheck'] == 2 else True
		else:
			self.data['rainCheck'] = False

	@property
	def rainCheck(self) -> bool:
		return self.data['rainCheck']

	@property
	def dailyAccumulation(self) -> Length:
		return self.data['localDailyAccumulationRainCheck'] if self.rainCheck else self.data['dailyAccumulationRaw']

	@property
	def dewpoint(self):
		try:
			value = self.data['dewpoint']
		except KeyError:
			value = Heat(dewpointCalc(self.temperature, self.humidity))
		return value.localized

	@property
	def feelsLike(self):
		return self.data['feelsLike']

	@property
	def airDensity(self):
		try:
			value = self.data['airDensity']
		except KeyError:
			value = classAtlas['airDensity'](airDensityCalc(self.temperature, self.pressure))
		return value


class LightningMessage(Observation):

	def __init__(self, udpData):
		self.messAtlas['data'] = 'evt'
		self.atlas = [*self.atlas, 'distance', 'energy']
		super(LightningMessage, self).__init__(udpData)
		delattr(self, 'atlas')
