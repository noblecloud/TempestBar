import logging
from datetime import datetime

import pytz

from constants import classAtlas
from units.defaults.weatherFlow import Heat, Wind
from units.length import Length
from units.others import Direction, Humidity, Lux, RadiantFlux, Volts
from units.pressure import Pressure
from units.time import Minute, Second


class WSObservation(dict):
	messAtlas = {'serial': 'serial_number',
	             'type':   'type',
	             'hub':    'hub_sn',
	             'data':   ''}
	atlas = ['time']

	def __init__(self, udpData):
		data = self.translate(udpData, self.messAtlas)
		if 'data' in data:
			data['data'] = self.convert(data['data'], self.atlas)
			data['time'] = datetime.fromtimestamp(int(data['data'].pop('time')), pytz.timezone('America/New_York'))
		super(WSObservation, self).__init__(data)

	@staticmethod
	def translate(udpData: dict, atlas: dict[str:str]):
		return {key: udpData[value] for key, value in atlas.items()}

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

	@property
	def data(self) -> dict:
		return self['data']

	def __setitem__(self, *args):
		logging.error('UDP Messages are immutable')


class _TempestMessage(WSObservation):
	@property
	def strikeDistance(self) -> Length:
		return self.data['strikeDistance']

	@property
	def windSampleInterval(self) -> Second:
		return self.data['windSampleInterval']

	@property
	def uvi(self) -> int:
		return self.data['uvi']

	@property
	def pressure(self) -> Pressure:
		return self.data['pressure']

	@property
	def battery(self) -> Volts:
		return self.data['battery']

	@property
	def reportInterval(self) -> Minute:
		return self.data['reportInterval']

	@property
	def illuminance(self) -> Lux:
		return self.data['illuminance']

	@property
	def precipitationType(self) -> str:
		value = self.data['precipitationType']
		if value == 1:
			value = 'Rain'
		elif value == 2:
			value = 'Hail'
		else:
			value = 'None'
		return value

	@property
	def strikes(self) -> int:
		return self.data['strikes']

	@property
	def temperature(self) -> Heat:
		return self.data['temperature']

	@property
	def humidity(self) -> Humidity:
		return self.data['humidity']

	@property
	def irradiance(self) -> RadiantFlux:
		return self.data['irradiance']

	@property
	def time(self) -> datetime:
		return self.data['time']

	@property
	def windDirection(self) -> Direction:
		return self.data['windDirection']

	@property
	def lull(self) -> Wind:
		return self.data['lullSpeed']

	@property
	def gust(self) -> Wind:
		return self.data['gustSpeed']

	@property
	def wind(self) -> Wind:
		return self.data['windSpeed']

	@property
	def precipRate(self) -> Length:
		return self.data['accumulation']


class WindMessage(WSObservation):

	def __init__(self, messageData):
		self.messAtlas['data'] = 'ob'
		self.atlas = [*self.atlas, 'speed', 'direction']
		super(WindMessage, self).__init__(messageData)
		delattr(self, 'atlas')

	@property
	def speed(self) -> Wind:
		return self['data']['speed']

	@property
	def direction(self) -> Direction:
		return self['data']['direction']

	@property
	def messsage(self):
		return 'Wind recorded {}km/h at {} ({}º)'.format(self.speed, self.direction.cardinal, self.direction)
