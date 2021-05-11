from json import dumps, loads
from secrets import token_urlsafe as genUUID

import websocket
from PySide2.QtCore import QObject, QThread, Signal
from PySide2.QtNetwork import QUdpSocket

from messages import *
from observer import Device, Station


class Messenger(QObject):
	signal: Signal = Signal(Observation)
	running: bool = False
	_station: Station

	messageTypes = {'rapid_wind': WindMessage, 'evt_precip': RainStartMessage, 'evt_strike': LightningMessage,
	                'obs_st':     TempestMessage, 'obs_sky': SkyMessage,
	                'hub_status': HubStatusMessage, 'device_status': DeviceStatusMessage}

	def testMessage(self):
		sample = {'serial_number': 'ST-00024322', 'type': 'obs_st', 'hub_sn': 'HB-00040538', 'obs': [[1612817710, 0.0, 0.49, 1.21, 117, 3, 1030.06, 4.16, 42.16, 12326, 0.4, 103, 0.0, 0, 0, 0, 2.825, 1]], 'firmware_revision': 134}
		# sample = {'serial_number': 'ST-00024322', 'type': 'device_status', 'hub_sn': 'HB-00040538', 'timestamp': 1612834329, 'uptime': 2876646, 'voltage': 2.73, 'firmware_revision': 134, 'rssi': -61, 'hub_rssi': -62, 'sensor_status': 8+16,
		#           'debug': 0}
		self.push(sample)

	def push(self, message: dict):
		if message['type'] in self.messageTypes:
			logging.debug("MESSAGE RECEIVED")
			messageType = self.messageTypes[message['type']]
			message = messageType(message)
			self.signal.emit(message)
		else:
			logging.debug("INVALID MESSAGE TYPE", message['type'])

	def setStation(self, value: Station):
		self._station = value


class WSMessenger(QThread, Messenger):
	token = '61173523-5a94-4392-bc6b-2e1d375d17fe'
	uri = 'wss://ws.weatherflow.com/swd/data?token=' + token
	uuid: str

	def __init__(self, parent=None):
		self.uuid = genUUID(8)
		super(WSMessenger, self).__init__(parent)
		self.WS = websocket.WebSocketApp(self.uri,
		                                 on_open=self.on_open,
		                                 on_message=self.on_message,
		                                 on_error=self.on_error,
		                                 on_close=self.on_close)

	def genMessage(self, messageType: str, device: Device) -> dict[str:str]:
		message = {"type":      messageType,
		         "device_id": device.deviceID,
		         "id":        self.uuid}
		return message

	def run(self):
		self.WS.run_forever()

	def begin(self):
		self.running = True
		self.start()

	def end(self):
		self.running = False
		self.WS.close()

	def on_open(self, ws):
		for device in self._station.observers:
			ws.send(dumps(self.genMessage('listen_start', device)))
			ws.send(dumps(self.genMessage('listen_rapid_start', device)))

	def on_message(self, ws, message):
		self.push(loads(message))

	def on_error(self, ws, error):
		print(error)

	def on_close(self, ws):
		print("### closed ###")

	def terminate(self):
		self.WS.close()


class UDPMessenger(Messenger):

	udpSocket: QUdpSocket

	def __init__(self, *args, **kwargs):
		super(UDPMessenger, self).__init__(*args, **kwargs)

	def begin(self):
		self.udpSocket = self.QUdpSocket(self)
		self.connectSocket()
		self.running = True
		self.listen()

	def end(self):
		self.running = False
		self.udpSocket.close()

	def connectSocket(self):
		self.udpSocket.bind(50222)
		self.udpSocket.readyRead.connect(self.listen)
		logging.info("UDP Connected to port: 50222")

	def listen(self):
		while self.udpSocket.hasPendingDatagrams():
			datagram, host, port = self.udpSocket.readDatagram(self.udpSocket.pendingDatagramSize())
			message = loads(str(datagram, encoding='ascii'))
			self.push(message)


web = True
if __name__ == '__main__' and web:
	ws = WSMessenger()
	ws.run()
elif __name__ == '__main__':
	from select import select
	from socket import AF_INET, INADDR_ANY, inet_aton, IP_ADD_MEMBERSHIP, IPPROTO_IP, IPPROTO_UDP, SO_REUSEADDR, SOCK_DGRAM, socket, SOL_SOCKET
	from struct import pack


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
