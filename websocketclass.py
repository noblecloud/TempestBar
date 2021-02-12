import asyncio
import json
from pprint import pprint

from PySide6.QtCore import QObject, Signal

import websockets

from constants import classAtlas
from messages import _TempestMessage, WindMessage, WSObservation
from units.defaults.weatherFlow import Precipitation


class TempestMessageWS(_TempestMessage):

	def __init__(self, messageData):
		self.messAtlas = {'deviceID': 'device_id',
		                  'type':     'type',
		                  'data':     'obs',
		                  'source':   'source',
		                  'summary':  'summary'}

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
		self.__delattr__('atlas')
		self.__delattr__('messAtlas')

	@property
	def rainCheck(self) -> bool:
		return self.data['rainCheck']

	@property
	def dailyAccumulation(self) -> Precipitation:
		return self.data['localDailyAccumulationRainCheck'] if self.rainCheck else self.data['dailyAccumulationRaw']


class WSMessenger(QObject):

	signal = Signal(WSObservation)

	token = 'f2f4cc66-7dec-4b09-bf64-f70c01da9690'
	uri = 'wss://ws.weatherflow.com/swd/data?token=' + token

	deviceID = 116322
	id = "59cb18db"

	def __init__(self, loop: asyncio.AbstractEventLoop, parent=None):
		super(WSMessenger, self).__init__(parent)
		self.loop = loop

	def start(self):
		asyncio.ensure_future(self.connectSocket(), loop=self.loop)

	def genMessage(self, messageType: str) -> dict[str:str]:
		return {"type":      messageType,
		        "device_id": self.deviceID,
		        "id":        self.id}

	async def connectSocket(self):
		async with websockets.connect(self.uri) as websocket:
			await websocket.send(json.dumps(self.genMessage('listen_start')))
			await websocket.send(json.dumps(self.genMessage('listen_rapid_start')))
			while True:
				message = json.loads(await websocket.recv())
				if message['type'] == 'rapid_wind':
					m = WindMessage(message)
					self.signal.emit(m)
					print(m.messsage)
				elif message['type'] == 'obs_st':
					m = TempestMessageWS(message)
					pprint(m)
					self.signal.emit(m)
				else:
					pprint(message)

	def work(self):
		asyncio.ensure_future(self.connectSocket(), loop=self.loop)


if __name__ == '__main__':
	pass
	loop = asyncio.get_event_loop()
	messenger = WSMessenger(loop)
	print('test')
