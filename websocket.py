# import asyncio
import json
from pprint import pprint

import websockets

from PySide6 import QtCore

token = 'f2f4cc66-7dec-4b09-bf64-f70c01da9690'
uri = 'wss://ws.weatherflow.com/swd/data?token=' + token

request = {
		"type":      "listen_start",
		"device_id": 116322,
		"id":        "59cb18db"
}

wind = {
		"type":      "listen_rapid_start",
		"device_id": 116322,
		"id":        "59cb18db"
}


# async def hello():
# 	async with websockets.connect(uri) as websocket:
# 		await websocket.send(json.dumps(request))
# 		await websocket.send(json.dumps(wind))
# 		while True:
# 			message = json.loads(await websocket.recv())
# 			pprint(message)
#
#
# asyncio.get_event_loop().run_until_complete(hello())
# asyncio.get_event_loop().run_forever()


class ListenWebsocket(QtCore.QThread):
	def __init__(self, parent=None):
		super(ListenWebsocket, self).__init__(parent)

		websockets.

		self.WS = websockets.WebSocketApp("ws://localhost:8080/chatsocket",
		                                 on_message=self.on_message,
		                                 on_error=self.on_error,
		                                 on_close=self.on_close)

	def run(self):
		# ws.on_open = on_open

		self.WS.run_forever()

	def on_message(self, ws, message):
		print
		message

	def on_error(self, ws, error):
		print
		error

	def on_close(self, ws):
		print
		"### closed ###"

# personal_token = ' '
# tempest_ID = ' '

# print('Opening Websocket connection...')
# ws = websockets.connect('wss://ws.weatherflow.com/swd/data?api_key=' + personal_token)
# result = ws.recv()
# print("Received '%s'" % result)
# print('')
#
# print('Listening to Tempest endpoint...')
# ws.send('{"type":"listen_start",' + ' "device_id":' + tempest_ID + ', "id":"Tempest"}')
# result =  ws.recv()
# print("Received '%s'" % result)
# print('')
#
# print('Receiving Tempest data...')
# while True:
#     result =  ws.recv()
#     print("Received '%s'" % result)
#     print('')
