from PySide6.QtCore import Signal, Slot, Qt
from PySide6.QtWidgets import QWidget

from messages import DeviceStatusMessage, HubStatusMessage, LightningMessage, Observation, TempestMessage, WindMessage
from observer import Station
from sockets import Messenger, WSMessenger
from ui.info_UI import Ui_info as InfoUI

import objc
from Foundation import *
from AppKit import *
from PyObjCTools import AppHelper


class QMacCocoaViewContainer(QWidget):
	""" QMacCocoaViewContainer(sip.voidptr, parent: QWidget = None) """

	def cocoaView(self):  # real signature unknown; restored from __doc__
		""" cocoaView(self) -> sip.voidptr """
		pass

	def setCocoaView(self, sip_voidptr):  # real signature unknown; restored from __doc__
		""" setCocoaView(self, sip.voidptr) """
		pass

	def __init__(self, sip_voidptr, parent=None):  # real signature unknown; restored from __doc__
		pass


class Info(QWidget, InfoUI):

	station: Station
	messenger: Messenger = WSMessenger()

	connectionSignal = Signal(bool)

	def __init__(self, *args, **kwargs):
		super(Info, self).__init__(*args, **kwargs)
		self.setupUi(self)
		self.skyGroup.setHidden(True)
		self.installEventFilter(self)
		self.setAttribute(Qt.WA_TranslucentBackground)
		self.messenger.signal.connect(self.updateItems)
		frame = NSMakeRect(0, 0, self.width(), self.height())
		view = objc.objc_object(c_void_p=self.winId().__int__())

		visualEffectView = NSVisualEffectView.new()
		visualEffectView.setAutoresizingMask_(NSViewWidthSizable | NSViewHeightSizable)
		visualEffectView.setWantsLayer_(True)
		visualEffectView.setFrame_(frame)
		visualEffectView.setState_(NSVisualEffectStateActive)
		visualEffectView.setMaterial_(NSVisualEffectMaterialHUDWindow)
		visualEffectView.setBlendingMode_(NSVisualEffectBlendingModeBehindWindow)
		visualEffectView.setWantsLayer_(True)

		self.setAttribute(Qt.WA_TranslucentBackground, True)

		window = view.window()
		content = window.contentView()

		container = QMacCocoaViewContainer(0, self)
		content.addSubview_positioned_relativeTo_(visualEffectView, NSWindowBelow, container)

		window.setTitlebarAppearsTransparent_(True)
		window.setStyleMask_(window.styleMask() | NSFullSizeContentViewWindowMask)

		appearance = NSAppearance.appearanceNamed_('NSAppearanceNameVibrantDark')
		window.setAppearance_(appearance)

		self.repaint()


	def toggle(self) -> bool:
		if not self.messenger.running:
			self.start()
		elif self.messenger.running:
			self.stop()

	@Slot(Station)
	def setStation(self, station: Station):
		self.messenger.setStation(station)

	def start(self):
		self.messenger.begin()

	def stop(self):
		if self.messenger.running:
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
			# self.setSkyGroup(event)
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
		self.window().menuBar.title = str(event.temperature)
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
