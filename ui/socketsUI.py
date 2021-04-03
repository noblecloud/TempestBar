from PySide6 import QtCore
from PySide6.QtCore import Slot
from PySide6.QtWidgets import QFrame, QGridLayout

from messages import Observation, TempestMessage, WindMessage
from sockets import UDPMessenger, WSMessenger
from websocket_UI import Ui_websocket


class Tab(QFrame):
	def __init__(self, *args, **kwargs):
		super(Tab, self).__init__(*args, **kwargs)
		self.setupUi(self)
		self.installEventFilter(self)
		self.messenger.signal.connect(self.updateItems)

	@Slot()
	def toggle(self):
		if self.messenger.running:
			self.messenger.stop()
		else:
			self.messenger.start()

	def eventFilter(self, obj, event):
		if event.type() == QtCore.QEvent.KeyPress:
			if event.key() == QtCore.Qt.Key_R:
				self.loop.create_task(self.messenger.connectSocket())
		return super(Tab, self).eventFilter(obj, event)


class UDPTab(Tab, Ui_websocket):

	def __init__(self, *args, **kwargs):
		self.messenger = UDPMessenger()
		super(UDPTab, self).__init__(*args, **kwargs)
		self.feelsLike.deleteLater()
		self.feelsLikeLabel.deleteLater()
		layout: QGridLayout = self.airGroup.layout()
		layout.takeAt(4)
		layout.takeAt(4)

	@Slot(Observation)
	def updateItems(self, event: Observation):

		if isinstance(event, WindMessage):
			value = '{} at {}'.format(event.direction.cardinal, event.speed.withUnit)
			self.wind.setText(value)
		if isinstance(event, TempestMessage):

			# Wind Group
			self.windAverage.setText(event.wind.withUnit)
			self.lull.setText(event.lullSpeed.withUnit)
			self.gust.setText(event.gustSpeed.withUnit)
			self.windDirection.setText('{} ({})'.format(event.windDirection.cardinal, event.windDirection.withUnit.strip(' ')))

			# Air
			self.temperature.setText(event.temperature.str)
			self.humidity.setText(event.humidity.str)
			self.pressure.setText(event.pressure.withUnit)
			self.airDensity.setText(event.airDensity.withUnit)
			self.dewpoint.setText(event.dewpoint.str)

			# Solar
			self.illuminance.setText(event.illuminance.withUnit)
			self.irradiance.setText(event.irradiance.withUnit)
			self.uv.setText(str(event.uvi))

			# Sky
			if event.strikes + event.accumulation > 0:
				self.skyGroup.setDisabled(False)
				if event.strikes:
					self.strikes.show()
					self.strikesLabel.show()
					self.strikeDistance.show()
					self.strikeDistanceLabel.show()
					self.strikes.setText(str(event.strikes))
					self.strikeDistance.setText(event.strikeDistance.withUnit)
				else:
					self.strikes.hide()
					self.strikesLabel.hide()
					self.strikeDistance.hide()
					self.strikeDistanceLabel.hide()

				if event.precipRate > 0:
					self.precipRate.show()
					self.precipRateLabel.show()
					self.precipRate.setText(event.accumulation.withUnit)
				else:
					self.precipRate.hide()
					self.precipRateLabel.hide()
				self.accumulationLabel.hide()
				self.accumulation.hide()
			else:
				self.skyGroup.setDisabled(True)

		# Status
		# self.deviceBattery.setText(event.battery.withUnit)

		# if isinstance(event, DeviceStatusMessage):
		# 	# 'uptime'
		# 	# 'firmware'
		# 	# 'rssi'
		# 	# 'battery'
		# 	# 'rssiHub'
		# 	# 'sensorStatus'
		#
		# 	self.deviceUptime.setText(event.uptime)
		# 	self.deviceBattery.setText(event.battery.withUnit)
		# 	self.deviceSerial.setText(event.serial)
		# 	self.deviceFirmware.setText(event.firmware)
		# 	self.deviceSensors.setText(str(event.sensorStatus))

		# if isinstance(event, HubStatusMessage):
		# 	self.hubUptime.setText(event.uptime)
		# 	self.hubSerial.setText(event.serial)
		# 	self.hubFirmware.setText(event.firmware)

		else:
			pass
# self.statusbar.showMessage(str(event))
# print(event)


class WSTab(Tab, Ui_websocket):

	def __init__(self, *args, **kwargs):
		self.messenger = WSMessenger()
		self.messenger.signal.connect(self.updateItems)
		super(WSTab, self).__init__(*args, **kwargs)

	@Slot(Observation)
	def updateItems(self, event: Observation):

		if isinstance(event, WindMessage):
			self.wind.setText(event.speed.withUnit)
			if event.speed != 0:
				self.windDirection.setText('{} ({}º)'.format(event.direction.cardinal, event.direction.withUnit.strip(' ')))


		if isinstance(event, TempestMessage):

			# Wind Group
			self.windAverage.setText(event.wind.withUnit)
			self.lull.setText(event.lullSpeed.withUnit)
			self.gust.setText(event.gustSpeed.withUnit)
			self.windDirectionAverage.setText('{} ({}º)'.format(event.windDirection.cardinal, event.windDirection.withUnit.strip(' ')))

			# Air
			self.temperature.setText(event.temperature.str)
			self.feelsLike.setText(event.feelsLike.str)
			self.humidity.setText(str(event.humidity))
			self.pressure.setText(event.pressure.withUnit)
			self.dewpoint.setText(event.dewpoint.withUnit)
			self.airDensity.setText(event.airDensity.withUnit)

			# Solar
			self.illuminance.setText(event.illuminance.withUnit)
			self.irradiance.setText(event.irradiance.withUnit)
			self.uv.setText(str(event.uvi))

			# Sky
			if event.strikes + event.accumulation > 0:
				self.skyGroup.setDisabled(False)
				if event.strikes:
					self.strikes.show()
					self.strikesLabel.show()
					self.strikeDistance.show()
					self.strikeDistanceLabel.show()
					self.strikes.setText(str(event.strikes))
					self.strikeDistance.setText(event.strikeDistance.withUnit)
				else:
					self.strikes.hide()
					self.strikesLabel.hide()
					self.strikeDistance.hide()
					self.strikeDistanceLabel.hide()

				if event.precipRate > 0:
					self.precipRate.show()
					self.precipRateLabel.show()
					self.precipRate.setText(event.accumulation.withUnit)
				else:
					self.precipRate.hide()
					self.precipRateLabel.hide()
				self.accumulationLabel.hide()
				self.accumulation.hide()
			else:
				self.skyGroup.setDisabled(True)

		# Status
		# self.deviceBattery.setText(event.battery.withUnit)

		# if isinstance(event, DeviceStatusMessage):
		# 	# 'uptime'
		# 	# 'firmware'
		# 	# 'rssi'
		# 	# 'battery'
		# 	# 'rssiHub'
		# 	# 'sensorStatus'
		#
		# 	self.deviceUptime.setText(event.uptime)
		# 	self.deviceBattery.setText(event.battery.withUnit)
		# 	self.deviceSerial.setText(event.serial)
		# 	self.deviceFirmware.setText(event.firmware)
		# 	self.deviceSensors.setText(str(event.sensorStatus))

		# if isinstance(event, HubStatusMessage):
		# 	self.hubUptime.setText(event.uptime)
		# 	self.hubSerial.setText(event.serial)
		# 	self.hubFirmware.setText(event.firmware)

		else:
			pass
# self.statusbar.showMessage(str(event))
# print(event)
# 	loop = asyncio.get_event_loop()
# 	self.messenger = WSMessenger(loop)
