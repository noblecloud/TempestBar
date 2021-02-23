from json import dumps, loads

from PySide6.QtCore import QObject, Signal

from messages import *
from pprint import pprint


class _Messenger(QObject):
	signal: Signal = Signal(Observation)
	messageTypes = {'rapid_wind': WindMessage, 'evt_precip': RainStartMessage, 'evt_strike': LightningMessage,
	                'obs_st':     TempestMessage, 'obs_air': AirMessage, 'obs_sky': SkyMessage,
	                'hub_status': HubStatusMessage, 'device_status': DeviceStatusMessage}

	def testMessage(self):
		sample = {'serial_number': 'ST-00024322', 'type': 'obs_st', 'hub_sn': 'HB-00040538', 'obs': [[1612817710, 0.0, 0.49, 1.21, 117, 3, 1030.06, 4.16, 42.16, 12326, 0.4, 103, 0.0, 0, 0, 0, 2.825, 1]], 'firmware_revision': 134}
		# sample = {'serial_number': 'ST-00024322', 'type': 'device_status', 'hub_sn': 'HB-00040538', 'timestamp': 1612834329, 'uptime': 2876646, 'voltage': 2.73, 'firmware_revision': 134, 'rssi': -61, 'hub_rssi': -62, 'sensor_status': 8+16,
		#           'debug': 0}
		self.push(sample)

	def push(self, message: dict):
		if message['type'] in self.messageTypes:
			messageType = self.messageTypes[message['type']]
			message = messageType(message)
			self.signal.emit(message)


class WSMessenger(_Messenger):
	import asyncio
	import websockets

	token = 'f2f4cc66-7dec-4b09-bf64-f70c01da9690'
	uri = 'wss://ws.weatherflow.com/swd/data?token=' + token

	deviceID = 116322
	id = "59cb18db"

	def __init__(self, loop: asyncio.AbstractEventLoop, parent=None):
		super(WSMessenger, self).__init__(parent)
		self.loop = loop

	def genMessage(self, messageType: str) -> dict[str:str]:
		return {"type":      messageType,
		        "device_id": self.deviceID,
		        "id":        self.id}

	async def listen(self):
		async with self.websockets.connect(self.uri) as websocket:
			await websocket.send(dumps(self.genMessage('listen_start')))
			await websocket.send(dumps(self.genMessage('listen_rapid_start')))
			while True:
				message = loads(await websocket.recv())
				self.push(message)

	def start(self):
		self.asyncio.ensure_future(self.listen(), loop=self.loop)


class UDPMessenger(_Messenger):
	from PySide6.QtNetwork import QUdpSocket

	udpSocket: QUdpSocket

	def __init__(self, *args, **kwargs):
		super(UDPMessenger, self).__init__(*args, **kwargs)

	def start(self):
		self.udpSocket = self.QUdpSocket(self)
		self.connectSocket()
		self.listen()

	def connectSocket(self):
		self.udpSocket.bind(50222)
		self.udpSocket.readyRead.connect(self.listen)

	def listen(self):
		while self.udpSocket.hasPendingDatagrams():
			datagram, host, port = self.udpSocket.readDatagram(self.udpSocket.pendingDatagramSize())
			message = loads(str(datagram, encoding='ascii'))
			self.push(message)


web = True

if __name__ == '__main__' and web:
	import asyncio
	loop = asyncio.get_event_loop()
	ws = WSMessenger(loop)
	asyncio.get_event_loop().run_until_complete(ws.connectSocket())
	asyncio.get_event_loop().run_forever()

elif __name__ == '__main__':
	from select import select
	from socket import AF_INET, INADDR_ANY, inet_aton, IP_ADD_MEMBERSHIP, IPPROTO_IP, IPPROTO_UDP, SO_REUSEADDR, SOCK_DGRAM, socket, SOL_SOCKET
	from struct import pack
	from time import sleep


	# create broadcast listener socket
	def create_broadcast_listener_socket(broadcast_ip, broadcast_port):
		b_sock = socket(AF_INET, SOCK_DGRAM, IPPROTO_UDP)
		b_sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

		b_sock.bind(('', broadcast_port))

		mreq = pack("4sl", inet_aton(broadcast_ip), INADDR_ANY)
		b_sock.setsockopt(IPPROTO_IP, IP_ADD_MEMBERSHIP, mreq)

		return b_sock


	BROADCAST_IP = '239.255.255.250'
	BROADCAST_PORT = 50222
	sock_list = [create_broadcast_listener_socket(BROADCAST_IP, BROADCAST_PORT)]

	try:
		while True:
			sleep(.1)
			readable, writable, exceptional = select(sock_list, [], sock_list, 0)
			for s in readable:
				data, addr = s.recvfrom(4096)
				data = loads(data)
				if data['type'] == 'evt_precip':
					m = RainStartMessage(data)
				if data['type'] == 'obs_st':
					m = TempestMessage(data)
				elif data['type'] == 'rapid_wind':  # and data['ob'][1] > 0:
					m = WindMessage(data)
				elif data['type'] not in ['hub_status', 'device_status', 'light_debug']:
					print(data)
				else:
					print(data)
	except KeyboardInterrupt:
		pass
