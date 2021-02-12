import asyncio
import json
from pprint import pprint

import websockets

from constants import classAtlas
from messages import _TempestMessage, WindMessage
from units.defaults.weatherFlow import Precipitation

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


class TempestMessageWS(_TempestMessage):

	def __init__(self, messageData):
		self.messAtlas = {'deviceID': 'device_id',
		             'type':   'type',
		             'data':   'obs',
		             'source': 'source',
		             'summary': 'summary'}

		self.atlas = [*self.atlas, 'lullSpeed', 'windSpeed', 'gustSpeed',
		              'windDirection', 'windSampleInterval', 'pressure',
		              'temperature', 'humidity', 'illuminance', 'uvi',
		              'irradiance', 'accumulation', 'precipitationType',
		              'strikeDistance', 'strikes', 'battery', 'reportInterval',
		              'dailyAccumulationRaw',
		              'dailyAccumulationRainCheck',
		              'localDailyAccumulationRainCheck',
		              'rainCheck']
		super(TempestMessageWS, self).__init__(messageData)

		summaryAtlas = {
				"feelsLike":                           "feels_like",
				"heatIndex":                           "heat_index",
				"dailyAccumulationYesterday":          "precip_accum_local_yesterday",
				"dailyAccumulationYesterdayRainCheck": "precip_accum_local_yesterday_final",
				"precipitationTypeYesterday":          "precip_analysis_type_yesterday",
				"accumulation1h":                      "precip_total_1h",
				"pressureTrend":                       "pressure_trend",
				# "pulse_adj_ob_temp":                   "pulse_adj_ob_temp",
				# "pulse_adj_ob_time":                   "pulse_adj_ob_time",
				# "pulse_adj_ob_wind_avg":               "pulse_adj_ob_wind_avg",
				# "rainingMinutes":                      "raining_minutes",
				"strikes1h":                           "strike_count_1h",
				"strikes3h":                           "strike_count_3h",
				"windChill":                           "wind_chill"
		}
		summary = self.translate(self.pop('summary'), summaryAtlas)
		summary = self.convert(summary, classAtlas)
		self['data'].update(summary)
		# Always assume rainCheck is on unless specified as false
		self['data']['rainCheck'] = False if self['data']['rainCheck'] == 2 else True

	@property
	def rainCheck(self) -> bool:
		return self.data['rainCheck']

	@property
	def dailyAccumulation(self) -> Precipitation:
		return self.data['localDailyAccumulationRainCheck'] if self.rainCheck else self.data['dailyAccumulationRaw']


async def connect():
	async with websockets.connect(uri) as websocket:
		await websocket.send(json.dumps(request))
		await websocket.send(json.dumps(wind))
		while True:
			message = json.loads(await websocket.recv())
			if message['type'] == 'rapid_wind':
				windMessage = WindMessage(message)
				print(windMessage.messsage)
			elif message['type'] == 'obs_st':
				m = TempestMessageWS(message)
				pprint(m)
			else:
				pprint(message)


asyncio.get_event_loop().run_until_complete(connect())
asyncio.get_event_loop().run_forever()

#
# class ListenWebsocket(QtCore.QThread):
# 	def __init__(self, parent=None):
# 		super(ListenWebsocket, self).__init__(parent)
#
# 		websockets.
#
# 		self.WS = websockets.WebSocketApp("ws://localhost:8080/chatsocket",
# 		                                 on_message=self.on_message,
# 		                                 on_error=self.on_error,
# 		                                 on_close=self.on_close)
#
# 	def run(self):
# 		# ws.on_open = on_open
#
# 		self.WS.run_forever()
#
# 	def on_message(self, ws, message):
# 		print
# 		message
#
# 	def on_error(self, ws, error):
# 		print
# 		error
#
# 	def on_close(self, ws):
# 		print
# 		"### closed ###"
#
# # personal_token = ' '
# # tempest_ID = ' '
#
# # print('Opening Websocket connection...')
# # ws = websockets.connect('wss://ws.weatherflow.com/swd/data?api_key=' + personal_token)
# # result = ws.recv()
# # print("Received '%s'" % result)
# # print('')
# #
# # print('Listening to Tempest endpoint...')
# # ws.send('{"type":"listen_start",' + ' "device_id":' + tempest_ID + ', "id":"Tempest"}')
# # result =  ws.recv()
# # print("Received '%s'" % result)
# # print('')
# #
# # print('Receiving Tempest data...')
# # while True:
# #     result =  ws.recv()
# #     print("Received '%s'" % result)
# #     print('')
