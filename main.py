import rumps
import WeatherUnits
from PySide6 import QtCore
from PySide6.QtCore import Signal
from PySide6.QtWidgets import QApplication, QMainWindow
from rumps import MenuItem

from ui.main_UI import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
	signal = Signal(str)
	menuBar: rumps.App

	def __init__(self, *args, **kwargs):
		super(MainWindow, self).__init__(*args, **kwargs)
		self.setupUi(self)
		self.connectionToggle.clicked.connect(self.toggle)

	def toggle(self):
		if self.stationSelection.isHidden():
			self.stationSelection.show()
		else:
			self.stationSelection.hide()

	def eventFilter(self, obj, event):
		if event.type() == QtCore.QEvent.KeyPress:
			if event.key() == QtCore.Qt.Key_R:
				self.loop.create_task(self.messenger.connectSocket())
		return super(MainWindow, self).eventFilter(obj, event)

	def exitHandler(self):
		self.webFrame.stop()
		self.udp.stop()


class TempestBar(rumps.App):
	app = QApplication()
	window = MainWindow()

	def __init__(self, title=None, icon=None, template=None, menu=None, quit_button='Quit'):
		super(TempestBar, self).__init__('NAº', title=None, icon=None, template=None, menu=None, quit_button='Quit')
		self.app.setQuitOnLastWindowClosed(False)
		self.window.menuBar = self
		self.app.aboutToQuit.connect(self.window.exitHandler)


	@rumps.clicked("Preferences")
	def prefs(self, _):
		rumps.alert("jk! no preferences available!")

	@rumps.clicked("Show Window")
	def display(self, sender):
		SECOND_DISPLAY = True
		if SECOND_DISPLAY:
			display = self.app.screens()[1]
			self.window.setScreen(display)
			self.window.move(display.geometry().x() + 200, display.geometry().y() + 200)
		self.window.show()

	@rumps.clicked('Connection', 'UDP')
	def udpSelected(self, _):
		self.window.tabs.setCurrentIndex(2)

	@rumps.clicked('Connection', 'WebSocket')
	def udpSelected(self, _):
		self.window.tabs.setCurrentIndex(1)

if __name__ == "__main__":
	WeatherUnits.config.read('config-example-us.ini')
	app = TempestBar("NAº")
	app.menu = [
			[rumps.MenuItem("Connection"),
			 [rumps.MenuItem("UDP"), rumps.MenuItem("WebSocket")]],
			None,
			rumps.MenuItem('Show Window')
	]
	app.display(app)
	app.run()
