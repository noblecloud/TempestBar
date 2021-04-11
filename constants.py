import math

from WeatherUnits.defaults.WeatherFlow import Wind
from WeatherUnits.defaults.WeatherFlow.units import Density, PrecipitationType, Temperature, Precipitation
from WeatherUnits.length import Kilometer, Millimeter
from WeatherUnits.others import Direction, Humidity, Lux, RadiantFlux, Volts
from WeatherUnits.pressure import mmHg, Pressure
from WeatherUnits.temperature import Celsius
from WeatherUnits.time import Minute, Second

classAtlas = {
		'time':                                int,

		'lullSpeed':                           Wind,
		'windSpeed':                           Wind,
		'gustSpeed':                           Wind,
		'speed':                               Wind,
		'direction':                           Direction,
		'windDirection':                       Direction,
		'windSampleInterval':                  Second,

		'temperature':                         Celsius,
		"feelsLike":                           Celsius,
		"heatIndex":                           Celsius,
		"windChill":                           Celsius,
		"dewpoint":                            Celsius,
		"wetbulb":                             Celsius,
		"delta_t":                             Celsius,
		'humidity':                            Humidity,
		'pressure':                            mmHg,
		"pressureTrend":                       str,
		"airDensity":                          Density,

		'illuminance':                         Lux,
		'uvi':                                 int,
		'irradiance':                          RadiantFlux,
		'accumulation':                        Millimeter,

		'distance':                            Kilometer,
		'strikeDistance':                      Kilometer,
		'strikeLastDistance':                  Kilometer,
		'strikeLastTime':                      int,
		'strikes':                             int,
		"strikes1h":                           int,
		"strikes3h":                           int,
		'energy':                              int,

		'battery':                             Volts,
		'reportInterval':                      Minute,

		'precipitationType':                   int,
		'rainingMinutes':                      list,
		'rainingTotalMinutes':                 Minute,
		'rainingTotalMinutesYesterday':        Minute,
		'dailyAccumulationRaw':                Millimeter,
		'dailyAccumulationRainCheck':          bool,
		'localDailyAccumulationRainCheck':     bool,
		"dailyAccumulationYesterday":          Millimeter,
		"dailyAccumulationYesterdayRainCheck": Millimeter,
		"precipitationTypeYesterday":          int,
		"accumulation1h":                      Precipitation,
		'rainCheck':                           int,

		"pulse_adj_ob_temp":                   Celsius,
		"pulse_adj_ob_time":                   int,
		"pulse_adj_ob_wind_avg":               Wind,
}

summaryAtlas = {
		'feels_like':                         'feelsLike',
		'heat_index':                         'heatIndex',
		'dew_point':                          'dewpoint',
		'wet_bulb_temperature':               'wetbulb',
		'precip_accum_local_yesterday':       'dailyAccumulationYesterday',
		'precip_accum_local_yesterday_final': 'dailyAccumulationYesterdayRainCheck',
		'precip_analysis_type_yesterday':     'precipitationTypeYesterday',
		'precip_total_1h':                    'accumulation1h',
		'pressure_trend':                     'pressureTrend',
		'air_density':                        'airDensity',
		# 'pulse_adj_ob_temp':                  'pulse_adj_ob_temp',
		# 'pulse_adj_ob_time':                  'pulse_adj_ob_time',
		# 'pulse_adj_ob_wind_avg':              'pulse_adj_ob_wind_avg',
		'raining_minutes':                    'rainingMinutes',
		"precip_minutes_local_day":           'rainingTotalMinutes',
		"precip_minutes_local_yesterday":     'rainingTotalMinutesYesterday',
		'strike_last_epoch':                  'strikeLastTime',
		'strike_last_dist':                   'strikeLastDistance',
		'strike_count_1h':                    'strikes1h',
		'strike_count_3h':                    'strikes3h',
		'wind_chill':                         'windChill'
}


def dewpointCalc(temperature: Celsius, rh: Humidity) -> Celsius:
	c = (243.04 * temperature.c / (17.625 + temperature.c)) + math.log(rh / 100.0)
	return Celsius((17.625 * c) / (243.04 - c))


def airDensityCalc(temperature: Celsius, pressure: Pressure):
	return (pressure.mb*100)/(temperature.kel*287.058)
