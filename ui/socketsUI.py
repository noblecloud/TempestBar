import logging

from PySide6 import QtCore
from PySide6.QtCore import QEvent, Signal, Slot
from PySide6.QtWidgets import QFrame, QGridLayout, QTabWidget, QWidget

from messages import DeviceStatusMessage, LightningMessage, Observation, TempestMessage, WindMessage, HubStatusMessage
from sockets import UDPMessenger, WSMessenger
from ui.socketTab_UI import Ui_socketTab


class Tab(QWidget, Ui_socketTab):

	connectionSignal = Signal(bool)

	def __init__(self, *args, **kwargs):
		super(Tab, self).__init__(*args, **kwargs)
		self.setupUi(self)
		self.skyGroup.setHidden(True)
		self.setMaximumSize(630, 368)
		self.installEventFilter(self)
		self.messenger.signal.connect(self.updateItems)

	def toggle(self) -> bool:
		if not self.messenger.running:
			self.start()
		elif self.messenger.running:
			self.stop()
		self.connectionSignal.emit(self.messenger.running)

	@Slot()
	def setStation(self, value):
		print(f'station set to: {value}')
		self.messenger.setStation(value)

	def start(self):
		self.messenger.begin()

	def stop(self):
		self.messenger.end()

	@property
	def running(self) -> bool:
		return self.messenger.running

	@Slot(Observation)
	def updateItems(self, event: Observation):

		if isinstance(event, WindMessage):
			self.receiveWind(event)

		if isinstance(event, LightningMessage):
			self.receiveLightning(event)

		if isinstance(event, TempestMessage):

			self.setWindGroup(event)
			self.setAirGroup(event)
			self.setSolarGroup(event)
			self.setSkyGroup(event)
		else:
			pass

	def setStatus(self, event):
		self.deviceBattery(event.battery)

		if isinstance(event, DeviceStatusMessage):
			# 'uptime'
			# 'firmware'
			# 'rssi'
			# 'battery'
			# 'rssiHub'
			# 'sensorStatus'

			self.deviceUptime(event.uptime)
			self.deviceBattery(event.battery)
			self.deviceSerial(event.serial)
			self.deviceFirmware(event.firmware)
			self.deviceSensors(event.sensorStatus)

		if isinstance(event, HubStatusMessage):
			self.hubUptime(event.uptime)
			self.hubSerial(event.serial)
			self.hubFirmware(event.firmware)

	def setSkyGroup(self, event):
		self.strikeTotal(event.strikes)
		self.strikeDistance(event.strikeDistance)
		self.rate(event.precipRate)
		if event.strikes + event.accumulation > 0:
			self.skyGroup.show()
			if event.strikes:
				self.skyGroup.lightning.show()
			else:
				self.skyGroup.lightning.hide()
			if event.precipRate + event.accumulation > 0:
				self.skyGroup.precipitation.show()
			else:
				self.skyGroup.precipitation.hide()

	def setSolarGroup(self, event):
		self.illuminance(event.illuminance)
		self.irradiance(event.irradiance)
		self.uv(event.uvi)

	def setAirGroup(self, event):
		self.temperature(event.temperature)
		self.feelsLike(event.feelsLike)
		self.dewpoint(event.dewpoint)
		self.humidity(event.humidity)
		self.pressure(event.pressure)
		self.airDensity(event.airDensity)

	def setWindGroup(self, event):
		self.windAverage(event.wind)
		self.lull(event.lullSpeed)
		self.gust(event.gustSpeed)
		self.windDirectionAverage(event.windDirection)

	def receiveLightning(self, event: LightningMessage):
		self.lastStrike(event.time)

	def receiveWind(self, event: WindMessage):
		self.wind(event.speed)
		if event.speed != 0:
			self.windDirection(event.direction)


class TabHolder(QTabWidget):

	tabSignal = Signal(Tab)

	@Slot(int)
	def sendTab(self, int):
		print('sending tab: ', end='')
		tab = self.currentWidget().layout().itemAt(0).widget()
		print(tab.__class__.__name__)
		self.tabSignal.emit(tab)


class UDPTab(Tab):

	def __init__(self, *args, **kwargs):
		self.messenger = UDPMessenger()
		super(UDPTab, self).__init__(*args, **kwargs)


class WSTab(Tab):

	def __init__(self, *args, **kwargs):
		self.messenger = WSMessenger()
		super(WSTab, self).__init__(*args, **kwargs)
