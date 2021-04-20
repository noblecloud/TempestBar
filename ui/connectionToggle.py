from PySide6.QtCore import Signal, Slot
from PySide6.QtWidgets import QPushButton
from ui.socketsUI import Tab


class connectionToggle(QPushButton):

	_connected: bool = False
	_currentTab: Tab = None

	def connection(self, status: bool):
		self._connected = status
		self.refreshText()

	@Slot(Tab)
	def changeChildTab(self, child: Tab):
		print(f"button received tab {child.__class__.__name__}")
		if self._currentTab and self._currentTab.running:
			self._currentTab.stop()
		self._currentTab = child
		self.refreshText(self._currentTab.running)


	@Slot(bool)
	def buttonClicked(self):

		# self._currentTab.start()
		print("Connect button clicked")
		self._currentTab.toggle()

	@Slot(bool)
	def refreshText(self, status: bool):
		print("refreshing text")
		if status:
			self.setText("Disconnect")
		else:
			self.setText("Connect")
