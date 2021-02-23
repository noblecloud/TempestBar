import asyncio
import sys

from PySide6 import QtCore
from PySide6.QtCore import Slot, Signal
from PySide6.QtWidgets import QApplication, QMainWindow
from qasync import QEventLoop

from messages import DeviceStatusMessage, HubStatusMessage, TempestMessage, WindMessage, Observation
from sockets import UDPMessenger, WSMessenger
from ui.main_UI import Ui_MainWindow

SECOND_DISPLAY = True


class MainWindow(QMainWindow, Ui_MainWindow):
	signal = Signal(str)
	UDP: bool = False

	def __init__(self, *args, **kwargs):
		super(MainWindow, self).__init__(*args, **kwargs)
		self.setupUi(self)
		self.installEventFilter(self)
		if self.UDP:
			self.messenger = UDPMessenger()
		else:
			loop = asyncio.get_event_loop()
			self.messenger = WSMessenger(loop)
		self.messenger.start()
		self.messenger.signal.connect(self.updateItems)

	def eventFilter(self, obj, event):
		if event.type() == QtCore.QEvent.KeyPress:
			if event.key() == QtCore.Qt.Key_R:
				self.loop.create_task(self.messenger.connectSocket())
				# print('testEvent')
				# self.updateItems(self.messenger.testMessage())
		return super(MainWindow, self).eventFilter(obj, event)

	@Slot(Observation)
	def receive_from_worker(self, message):
		print('message received')

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
			self.humidity.setText(str(event.humidity))
			self.pressure.setText(event.pressure.withUnit)

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
		self.statusbar.showMessage(str(event))
		print(event)


if __name__ == '__main__':
	app = QApplication()
	loop = QEventLoop(app)
	asyncio.set_event_loop(loop)
	window = MainWindow()

	if SECOND_DISPLAY:
		display = app.screens()[1]
		window.setScreen(display)
		window.move(display.geometry().x() + 200, display.geometry().y()+200)
	window.show()
	with loop:
		loop.run_forever()

	sys.exit(app.exec_())
