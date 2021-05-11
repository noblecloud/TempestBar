from abc import ABC
from typing import Callable

from PySide2.QtCore import Signal
from rumps import MenuItem
from observer import Device, Station, StationList


# class DeviceItem(MenuItem, ABC):
# 	_device: Device
# 	_signal: Signal
#
# 	def toggle(self, sender):
# 		self._device.enabled = self.state = not self.state
# 		self._signal.emit(self._device.station)
#
# 	def __init__(self, device: Device, signal: Signal):
# 		super(DeviceItem, self).__init__(device.name)
# 		self._device = device
# 		self._signal = signal
	# self.set_callback(self.toggle)


class StationItem(MenuItem, ABC):
	_station: Station

	def __init__(self, station: Station, callback: Callable):
		super(StationItem, self).__init__(station.name, callback=callback)
		self._station = station

	@property
	def state(self):
		return self._menuitem.state()

	@state.setter
	def state(self, new_state):
		self._menuitem.setState_(new_state)
		self._station.enabled = bool(new_state)


class StationSelector(MenuItem, ABC):
	_signal: Signal
	_devices: StationList

	def __init__(self, signal: Signal):
		super(StationSelector, self).__init__("Stations")
		self._signal = signal
		self.buildMenu()
		true = True
		default = self.values()[0]
		default.state = true
		self._signal.emit(default._station)

	def buildMenu(self):
		stations = self._getStations()
		for station in stations:
			self.add(StationItem(station, self.toggle))

	def toggle(self, sender: StationItem):
		sender.state = not sender.state
		if sender.state:
			print(f'emitting {sender._station.name}')
			self._signal.emit(sender._station)

	@classmethod
	def _getStations(cls) -> StationList:
		import urllib.request

		url = 'https://swd.weatherflow.com/swd/rest/stations/'
		token = "f2f4cc66-7dec-4b09-bf64-f70c01da9690"

		devices = {}
		url = "{}?token={}".format(url, token)
		with urllib.request.urlopen(url) as response:
			return StationList(response.read())
