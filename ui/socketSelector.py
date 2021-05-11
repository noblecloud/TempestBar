from abc import ABC
from typing import Callable

from PySide6.QtCore import Signal, Slot
from rumps import MenuItem

from sockets import Messenger, UDPMessenger, WSMessenger


class SocketItem(MenuItem, ABC):
	_socket: Messenger

	def __init__(self, text: str, socket: Messenger, callback: Callable):
		super(SocketItem, self).__init__(text, callback=callback)
		self._socket = socket
		self.set_callback(callback)

	@property
	def socket(self):
		return self._socket


class SocketSelector(MenuItem, ABC):
	_signal: Signal

	def __init__(self, signal: Signal):
		super(SocketSelector, self).__init__('Connection')
		self._signal = signal
		self.buildMenu()

	def _callback(self, sender: SocketItem):
		self._signal.emit(sender.socket)
		for item in self.items():
			if item[1].title != sender.title:
				item[1].state = False
			else:
				item[1].state = True

	def buildMenu(self):
		self.add(SocketItem('UDP', UDPMessenger(), self._callback))
		web = SocketItem('WebSocket', WSMessenger(), self._callback)
		web.state = True
		self.add(web)
