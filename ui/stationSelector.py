from PySide6.QtCore import Signal, Slot
from PySide6.QtWidgets import QComboBox

from observer import Station, StationList


class StationSelector(QComboBox):

	stationSelection = Signal(Station)
	_devices: StationList

	def __init__(self, *args, **kwargs):
		super(StationSelector, self).__init__(*args, **kwargs)
		self._devices = self._getDevices()
		for device in self._devices:
			self.addItem(device.name, device)
		self.currentIndexChanged.connect(self.convertSelection)
		self.activated.connect(self.convertSelection)

	def _getDevices(self) -> StationList:
		import urllib.request

		url = 'https://swd.weatherflow.com/swd/rest/stations/'
		token = "f2f4cc66-7dec-4b09-bf64-f70c01da9690"

		devices = {}
		url = "{}?token={}".format(url, token)
		with urllib.request.urlopen(url) as response:
			return StationList(response.read())

	def currentData(self, **kwargs) -> Station:
		return super(StationSelector, self).currentData(**kwargs)

	@Slot(int)
	def convertSelection(self, index: int):
		self.stationSelection.emit(self.currentData())
