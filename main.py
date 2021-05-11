import rumps
import WeatherUnits
from PySide6.QtCore import Property, QAbstractAnimation, QEvent, QPropertyAnimation, QTimer, Signal, Slot, Qt
from PySide6.QtGui import QCursor
from PySide6.QtWidgets import QApplication, QMainWindow
from rumps import MenuItem

from observer import Station
from sockets import Messenger
from ui.main_UI import Ui_MainWindow
from ui.socketSelector import SocketSelector
from ui.stationSelector import StationSelector

import AppKit
info = AppKit.NSBundle.mainBundle().infoDictionary()
info["LSBackgroundOnly"] = "1"




class MainWindow(QMainWindow, Ui_MainWindow):
	menuBar: rumps.App
	stationSignal = Signal(Station)
	socketSignal = Signal(Messenger)
	_station: Station
	_value = 0
	timer = QTimer()

	valueChanged = Signal(int)

	def __init__(self, *args, **kwargs):
		super(MainWindow, self).__init__(*args, **kwargs)
		self.setupUi(self)

		self.setWindowFlag(Qt.FramelessWindowHint)
		self.setWindowFlag(Qt.WindowStaysOnTopHint)
		self.setFocusPolicy(Qt.StrongFocus)
		self.installEventFilter(self)
		self.setStyleSheet('color: white')
		self.draggable = True
		self.dragging_threshould = 5
		self.__mousePressPos = None
		self.__mouseMovePos = None
		self.timer.timeout.connect(self.poop)
		self.anim = QPropertyAnimation(self, b"value")
		self.animationFinished()
		self.anim.finished.connect(self.animationFinished)
		self.setWindowModality(Qt.WindowModality.NonModal)

		self.setAttribute(Qt.WA_TranslucentBackground)

	def animationFinished(self):
		if self._value == 0:
			self.timer.stop()
			# super().hide()
			self.anim.setDuration(70)
			self.anim.setEndValue(1000)
		else:
			# self.anim.setDirection(QAbstractAnimation.Direction.Forward)
			self.anim.setDuration(500)
			self.anim.setEndValue(0)

	@Property(int)
	def value(self):
		return self._value

	@value.setter
	def value(self, value):
		self.setWindowOpacity(value/1000.0)
		print(value)
		self._value = value
		if value < 5:
			super().hide()
		else:
			super().show()

	def poop(self):
		print('poop')
		self.hide()
		# self.timer.stop()
		# print('poop')

	# def mousePressEvent(self, event):
	# 	if self.draggable and event.button() == QtCore.Qt.LeftButton:
	# 		self.__mousePressPos = event.globalPos()  # global
	# 		self.__mouseMovePos = event.globalPos() - self.pos()  # local
	# 	super(MainWindow, self).mousePressEvent(event)
	#
	# def mouseMoveEvent(self, event):
	# 	if self.draggable and event.buttons() & QtCore.Qt.LeftButton:
	# 		globalPos = event.globalPos()
	# 		moved = globalPos - self.__mousePressPos
	# 		if moved.manhattanLength() > self.dragging_threshould:
	# 			# move when user drag window more than dragging_threshould
	# 			diff = globalPos - self.__mouseMovePos
	# 			self.move(diff)
	# 			self.__mouseMovePos = globalPos - self.pos()
	# 	super(MainWindow, self).mouseMoveEvent(event)
	#
	# def mouseReleaseEvent(self, event):
	# 	if self.__mousePressPos is not None:
	# 		if event.button() == QtCore.Qt.LeftButton:
	# 			moved = event.globalPos() - self.__mousePressPos
	# 			if moved.manhattanLength() > self.dragging_threshould:
	# 				# do not call click event or so on
	# 				event.ignore()
	# 			self.__mousePressPos = None
	# 	super(MainWindow, self).mouseReleaseEvent(event)
	#
	# 	# close event
	# 	if event.button() == QtCore.Qt.RightButton:
	# 		QtGui.qApp.exit()

	def hide(self):
		self.anim.setDirection(QAbstractAnimation.Direction.Forward)
		self.anim.start()
		# self.menuBar['Hide Window'].title = 'Show Window'

	def show(self):
		self.anim.start()

	def eventFilter(self, obj, event):
		if event.type() == QEvent.KeyPress:
			if event.key() == Qt.Key_R:
				self.websocket.toggle()
			if event.key() == Qt.Key_T:
				self.setWindowOpacity(100)
		if event.type() == QEvent.HoverMove:
			self.timer.start(1000)
		if event.type() == QEvent.HoverEnter:
			self.timer.timeout.disconnect(self.poop)
		if event.type() == QEvent.HoverLeave:
			self.timer.timeout.connect(self.poop)

		return super(MainWindow, self).eventFilter(obj, event)

	def focusOutEvent(self, QEvent):
		self.hide()

	def enterEvent(self, event):
		self.timer.stop()

	@Slot(Station)
	def receiveStation(self, station):
		self.info.stop()
		self.info.setStation(station)
		self._station = station
		self.info.start()

	@Slot(Messenger)
	def receiveSocket(self, socket):
		self.info.stop()
		self.info.messenger = socket
		self.receiveStation(self._station)

	def exitHandler(self):
		self.webFrame.stop()
		self.udp.stop()


class TempestBar(rumps.App):
	showHide: MenuItem
	app = QApplication()
	window = MainWindow()

	def __init__(self, title=None, icon=None, template=None, menu=None, quit_button='Quit'):
		super(TempestBar, self).__init__('NAº', title=None, icon=None, template=None, menu=None, quit_button='Quit')
		self.app.setQuitOnLastWindowClosed(False)
		self.window.menuBar = self
		self.app.aboutToQuit.connect(self.window.exitHandler)
		self.window.socketSignal.connect(self.window.receiveSocket)
		self.window.stationSignal.connect(self.window.receiveStation)
		self.menu.add(SocketSelector(self.window.socketSignal))
		self.menu.add(StationSelector(self.window.stationSignal))
		self.showHide = rumps.MenuItem('Show Window', callback=self.display)
		self.menu.add(self.showHide)

	def updateMenus(self):
		if self.window.isHidden():
			self.showHide.title = "Hide Window"
		else:
			self.showHide.title = "Show Window"

	def display(self, sender):
		if self.window.isHidden():
			self.window.move(QCursor().pos().x() - 50, 0)
			self.window.show()
			self.window.setEnabled(True)
			self.window.setFocus(Qt.FocusReason.PopupFocusReason)
		else:
			self.window.hide()

	@rumps.clicked('Connection')
	def udpSelected(self, sender):
		print(sender)



if __name__ == "__main__":
	WeatherUnits.config.read('config-example-us.ini')
	app = TempestBar("NAº")
	print(app.menu)
	# app.display(app.menu['Show Window'])
	app.run()
