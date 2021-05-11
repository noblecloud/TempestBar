from PySide2.QtCore import Signal, Slot
from PySide2.QtWidgets import QPushButton


class connectionToggle(QPushButton):

	_connected: bool = False

	def connection(self, status: bool):
		self._connected = status
		self.refreshText()

	@Slot()
	def changeChildTab(self, child):
		print(f"button received tab {child.__class__.__name__}")
		if self._currentTab and self._currentTab.running:
			self._currentTab.stop()
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
