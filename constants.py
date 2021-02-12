from units.defaults.weatherFlow import *
from units.others import Direction, Humidity, Lux, RadiantFlux, Volts
from units.time import Minute, Second

classAtlas = {
		'time':                                int,

		'lullSpeed':                           Wind,
		'windSpeed':                           Wind,
		'gustSpeed':                           Wind,
		'speed':                               Wind,
		'direction':                           Direction,
		'windDirection':                       Direction,
		'windSampleInterval':                  Second,

		'temperature':                         Heat,
		"feelsLike":                           Heat,
		"heatIndex":                           Heat,
		"windChill":                           Heat,
		'humidity':                            Humidity,
		'pressure':                            mmHg,
		"pressureTrend":                       str,

		'illuminance':                         Lux,
		'uvi':                                 int,
		'irradiance':                          RadiantFlux,
		'accumulation':                        Precipitation,

		'precipitationType':                   PrecipitationType,
		'distance':                            Kilometer,
		'strikeDistance':                      Kilometer,
		'strikes':                             int,
		"strikes1h":                           int,
		"strikes3h":                           int,
		'energy':                              int,

		'battery':                             Volts,
		'reportInterval':                      Minute,
		'dailyAccumulationRaw':                Precipitation,
		'dailyAccumulationRainCheck':          bool,
		'localDailyAccumulationRainCheck':     bool,
		"dailyAccumulationYesterday":          Millimeter,
		"dailyAccumulationYesterdayRainCheck": Millimeter,
		"precipitationTypeYesterday":          PrecipitationType,
		"accumulation1h":                      Precipitation,
		'rainCheck':                           int,

		"pulse_adj_ob_temp":                   Heat,
		# "pulse_adj_ob_time":                   "pulse_adj_ob_time",
		"pulse_adj_ob_wind_avg":               Wind
		# "rainingMinutes":                      "raining_minutes",
}
