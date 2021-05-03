import datetime
from typing import Union


class Device:
	deviceID: int
	serialNumber: str
	locationID: int
	hardwareRevision: int
	firmwareRevision: int
	name: str

	def __init__(self, data: dict):
		self.deviceID = data['device_id']
		self.serialNumber = data['serial_number']
		self.locationID = data['location_id']
		hardwareRevision = data['hardware_revision']
		firmwareRevision = data['firmware_revision']
		self.name = data['device_meta']['name']

	def __repr__(self) -> str:
		return self.name

	def __str__(self) -> str:
		return self.name


class Hub(Device):
	deviceType = "hub"

	def __init__(self, data):
		super(Hub, self).__init__(data)


class Observer(Device):
	deviceType = "station"

	def __init__(self, *args, **kwargs):
		super(Observer, self).__init__(*args, **kwargs)



class Station(dict):
	_hub: Hub
	_observers: list[Observer] = []
	_defaultDevice: Observer

	def __init__(self, data):

		devices = data.pop('devices')

		for device in devices:
			deviceType = device['device_type']
			if deviceType == 'HB':
				self._hub = Hub(device)
			if deviceType == 'ST':
				observer = Observer(device)
				self._observers.append(observer)
				self._defaultDevice = observer
		super(Station, self).__init__({**data, 'hub': self._hub, 'observers': self._observers})

	@property
	def hub(self) -> Hub:
		return self._hub

	@property
	def observers(self) -> list[Observer]:
		return self._observers

	@property
	def name(self):
		return self['name']

	@property
	def stationID(self):
		return self['station_id']

	@property
	def lastUpdate(self):
		return datetime.datetime.fromtimestamp(self['last_modified_epoch'])

	@property
	def subscriptionID(self):
		return list(station.deviceID for station in self._observers)

	@property
	def defaultDevice(self) -> Observer:
		return self._defaultDevice



class StationList(list[Station]):

	def __init__(self, data: Union[dict, bytes]):
		if isinstance(data, bytes):
			from json import loads
			data = loads(data.decode('ascii'))

		if not isinstance(data, list):
			data = data['stations']
		super(StationList, self).__init__(Station(station) for station in data)

	@property
	def names(self) -> list[str]:
		return list(station.name for station in self)
