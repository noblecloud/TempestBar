import logging
from datetime import datetime, timedelta
from json import loads
from select import select
from socket import AF_INET, INADDR_ANY, inet_aton, IP_ADD_MEMBERSHIP, IPPROTO_IP, IPPROTO_UDP, SO_REUSEADDR, SOCK_DGRAM, socket, SOL_SOCKET
from struct import pack
from time import sleep

import pytz
from PySide6.QtCore import QObject, Signal
from PySide6.QtNetwork import QUdpSocket

from constants import classAtlas
from units.defaults.weatherFlow import *
from units.length import Length
from units.others import Direction, Humidity, Lux, RadiantFlux, Volts
from units.pressure import Pressure
from units.time import Minute, Second


class UDPObservation(dict):
	messAtlas = {'serial': 'serial_number',
	             'type':   'type',
	             'hub':    'hub_sn',
	             'data':   ''}
	atlas = ['time']

	def __init__(self, udpData):
		data = {key: udpData[value] for key, value in self.messAtlas.items()}
		if 'data' in data:
			data['data'] = self.convert(data['data'])
			data['time'] = datetime.fromtimestamp(int(data['data'].pop('time')), pytz.timezone('America/New_York'))
		super(UDPObservation, self).__init__(data)

	def convert(self, data):
		if isinstance(data[0], list):
			data = data[0]
		converted = {}
		for key, value in zip(self.atlas, data):
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


class UDPStatus(dict):
	atlas = {'time':     'timestamp',
	         'type':     'type',
	         'serial':   'serial_number',
	         'uptime':   'uptime',
	         'firmware': 'firmware_revision',
	         'rssi':     'rssi',
	         }

	def __init__(self, udpData):
		data = {key: udpData[value] for key, value in self.atlas.items()}
		super(UDPStatus, self).__init__(data)

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


class DeviceStatusMessage(UDPStatus):
	atlas = {**UDPStatus.atlas,
	         'serialHub':    'hub_sn',
	         'battery':      'voltage',
	         'rssiHub':      'hub_rssi',
	         'sensorStatus': 'sensor_status',
	         'debug':        'debug'
	         }

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

class HubStatusMessage(UDPStatus):
	def __init__(self, udpData):
		super(HubStatusMessage, self).__init__(udpData)


class RainStartMessage(UDPObservation):

	def __init__(self, udpData):
		self.messAtlas['data'] = 'evt'
		super().__init__(udpData)

	def print(self):
		print('Rain event started')


class WindMessage(UDPObservation):

	def __init__(self, udpData):
		self.messAtlas['data'] = 'ob'
		self.atlas = [*self.atlas, 'speed', 'direction']
		super(WindMessage, self).__init__(udpData)
		delattr(self, 'atlas')

	def print(self):
		print('Wind recorded {}km/h at {}º'.format(self['data']['speed'], self['data']['direction']))

	@property
	def speed(self) -> Wind:
		return self['data']['speed']

	@property
	def direction(self) -> Direction:
		return self['data']['direction']


class LightMessage(UDPObservation):
	"""
	I haven't quite figured out what this message contains.
	I am confident the item at index 2 is irradiance, but the
	item a index 1 alludes me.  It could be illuminance, but I
	can not figure out what the unit is.
	"""

	def __init__(self, udpData):
		self.messAtlas['data'] = 'ob'
		self.atlas = [*self.atlas, 'illuminance', 'irradiance', 'zero', 'zero']
		super(LightMessage, self).__init__(udpData)
		delattr(self, 'atlas')


class UDPMultiObservation(UDPObservation):
	pass


class AirMessage(UDPObservation):

	def __init__(self, udpData):
		self.messAtlas['data'] = 'obs'
		self.atlas = [*self.atlas, 'pressure', 'temperature', 'humidity', 'lightning',
		              'lightningDistance', 'battery', 'reportInterval']
		super(AirMessage, self).__init__(udpData)


class SkyMessage(UDPObservation):

	def __init__(self, udpData):
		self.messAtlas['data'] = 'obs'
		self.atlas = [*self.atlas, 'illuminance', 'uvi', 'accumulation', 'lullSpeed', 'windSpeed',
		              'gustSpeed', 'windDirection', 'battery', 'reportInterval', 'irradiance',
		              'accumulationDay', 'precipitationType', 'windSampleInterval']

		super(SkyMessage, self).__init__(udpData)

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
	def gustSpeed(self) -> Wind:
		return self.data['gustSpeed']

	@property
	def windDirection(self) -> int:
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
	def accumulationDay(self) -> Length:
		return self.data['accumulationDay']

	@property
	def precipitationType(self) -> int:
		return self.data['precipitationType']

	@property
	def windSampleInterval(self) -> Second:
		return self.data['windSampleInterval']


class TempestMessage(UDPObservation):

	def __init__(self, udpData):
		self.messAtlas['data'] = 'obs'
		self.atlas = [*self.atlas, 'lullSpeed', 'windSpeed', 'gustSpeed', 'windDirection',
		              'windSampleInterval', 'pressure', 'temperature', 'humidity',
		              'illuminance', 'uvi', 'irradiance', 'accumulation',
		              'precipitationType', 'strikeDistance', 'strikes',
		              'battery', 'reportInterval']
		super(TempestMessage, self).__init__(udpData)

	@property
	def uvi(self) -> int:
		return self.data['uvi']

	@property
	def precipRate(self) -> Length:
		return self.data['accumulation']

	@property
	def lull(self) -> Wind:
		return self.data['lullSpeed']

	@property
	def wind(self) -> Wind:
		return self.data['windSpeed']

	@property
	def gust(self) -> Wind:
		return self.data['gustSpeed']

	@property
	def windDirection(self) -> Direction:
		return self.data['windDirection']

	@property
	def battery(self) -> Volts:
		return self.data['battery']

	@property
	def irradiance(self) -> RadiantFlux:
		return self.data['irradiance']

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
	def windSampleInterval(self) -> Second:
		return self.data['windSampleInterval']

	@property
	def time(self) -> datetime:
		return self.data['time']

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

	@property
	def reportInterval(self) -> Minute:
		return self.data['reportInterval']


class LightningMessage(UDPObservation):

	def __init__(self, udpData):
		self.messAtlas['data'] = 'evt'
		self.atlas = [*self.atlas, 'distance', 'energy']
		super(LightningMessage, self).__init__(udpData)
		delattr(self, 'atlas')


class UDPMessenger(QObject):
	signal: Signal = Signal(UDPObservation)
	messageTypes = {'rapid_wind': WindMessage, 'evt_precip': RainStartMessage, 'evt_strike': LightningMessage,
	                'obs_st':     TempestMessage, 'obs_air': AirMessage, 'obs_sky': SkyMessage,
	                'hub_status': HubStatusMessage, 'device_status': DeviceStatusMessage}

	def __init__(self, *args, **kwargs):
		super(UDPMessenger, self).__init__(*args, **kwargs)
		self.udpSocket = QUdpSocket(self)
		self.connectUPD()

	def connectUPD(self):
		self.udpSocket.bind(50222)
		self.udpSocket.readyRead.connect(self.receiveUDP)

	def receiveUDP(self):
		while self.udpSocket.hasPendingDatagrams():
			datagram, host, port = self.udpSocket.readDatagram(self.udpSocket.pendingDatagramSize())
			datagram = loads(str(datagram, encoding='ascii'))
			if datagram['type'] in self.messageTypes:
				messageType = self.messageTypes[datagram['type']]
				message = messageType(datagram)
				self.signal.emit(message)

	def testMessage(self):
		sample = {'serial_number': 'ST-00024322', 'type': 'obs_st', 'hub_sn': 'HB-00040538', 'obs': [[1612817710, 0.0, 0.49, 1.21, 117, 3, 1030.06, 4.16, 42.16, 12326, 0.4, 103, 0.0, 0, 0, 0, 2.825, 1]], 'firmware_revision': 134}
		# sample = {'serial_number': 'ST-00024322', 'type': 'device_status', 'hub_sn': 'HB-00040538', 'timestamp': 1612834329, 'uptime': 2876646, 'voltage': 2.73, 'firmware_revision': 134, 'rssi': -61, 'hub_rssi': -62, 'sensor_status': 8+16,
		#           'debug': 0}
		messageType = self.messageTypes[sample['type']]
		return messageType(sample)


# create broadcast listener socket
def create_broadcast_listener_socket(broadcast_ip, broadcast_port):
	b_sock = socket(AF_INET, SOCK_DGRAM, IPPROTO_UDP)
	b_sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

	b_sock.bind(('', broadcast_port))

	mreq = pack("4sl", inet_aton(broadcast_ip), INADDR_ANY)
	b_sock.setsockopt(IPPROTO_IP, IP_ADD_MEMBERSHIP, mreq)

	return b_sock


if __name__ == '__main__':

	BROADCAST_IP = '239.255.255.250'
	BROADCAST_PORT = 50222
	sock_list = [create_broadcast_listener_socket(BROADCAST_IP, BROADCAST_PORT)]

	try:
		while True:
			sleep(.1)
			readable, writable, exceptional = select(sock_list, [], sock_list, 0)
			for s in readable:
				data, addr = s.recvfrom(4096)
				data = loads(data)
				if data['type'] == 'evt_precip':
					m = RainStartMessage(data)
				if data['type'] == 'obs_st':
					m = TempestMessage(data)
				elif data['type'] == 'rapid_wind':  # and data['ob'][1] > 0:
					m = WindMessage(data)
					m.print()
				elif data['type'] not in ['hub_status', 'device_status', 'light_debug']:
					print(data)
				else:
					print(data)
	except KeyboardInterrupt:
		pass
