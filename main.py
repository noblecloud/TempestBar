import sys
from PySide6 import QtCore
from PySide6.QtCore import Signal
from PySide6.QtWidgets import QApplication, QMainWindow

from ui.main_UI import Ui_MainWindow

SECOND_DISPLAY = True


class MainWindow(QMainWindow, Ui_MainWindow):
	signal = Signal(str)

	def __init__(self, *args, **kwargs):
		super(MainWindow, self).__init__(*args, **kwargs)
		self.devices = self.getDevices()
		print(list(self.devices.keys()))
		self.setupUi(self)
		# self.comboBox_2.addItems(list(self.devices.keys()))
		# for item in self.devices.keys():
		self.comboBox_2.addItem(str(list(self.devices.keys())[0]))
		self.connectionToggle_2.clicked.connect(self.toggle)

	def getDevices(self):
		import urllib.request
		from json import loads

		url = 'https://swd.weatherflow.com/swd/rest/stations/'
		token = "f2f4cc66-7dec-4b09-bf64-f70c01da9690"

		devices = {}
		url = "{}?token={}".format(url, token)
		with urllib.request.urlopen(url) as response:
			the_page: bytes = response.read()
			data = loads(the_page.decode('ascii'))
			for x in data['stations']:
				for y in x['devices']:
					if y['device_type'] != 'HB':
						id = y.pop('device_id')
						devices[id] = y
		return devices

	def toggle(self):
		if self.tabs.currentWidget().objectName() == 'udp':
			self.udpFrame.toggle()
		elif self.tabs.currentWidget().objectName() == 'webSocket':
			self.webFrame.toggle()

	def eventFilter(self, obj, event):
		if event.type() == QtCore.QEvent.KeyPress:
			if event.key() == QtCore.Qt.Key_R:
				self.loop.create_task(self.messenger.connectSocket())
		return super(MainWindow, self).eventFilter(obj, event)

	def exitHandler(self):
		self.webFrame.messenger.terminate()


if __name__ == '__main__':
	import logging
	app = QApplication()
	app.setQuitOnLastWindowClosed(True)
	window = MainWindow()
	app.aboutToQuit.connect(window.exitHandler)

	if SECOND_DISPLAY:
		display = app.screens()[1]
		window.setScreen(display)
		window.move(display.geometry().x() + 200, display.geometry().y() + 200)
	window.show()

	sys.exit(app.exec_())
