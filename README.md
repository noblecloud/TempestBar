# TempestBar
A very simple proof of concept for displaying UDP data on a desktop using Python3 and PySide2.

## Requirements
 - [Python 3.9](https://www.python.org/downloads/)
 - [PySide2](https://pypi.org/project/PySide2/)
 - [WeatherUnits](https://pypi.org/project/WeatherUnits/)
 - [websockets](https://pypi.org/project/websockets/)
 - [pytz](https://pypi.org/project/pytz/)
 - WeatherFlow Station (only tested with [Tempest](https://weatherflow.com/tempest-weather-system/))

## Usage
Install PySide2 with

	pip install PySide2

Run with

	python main.py

## TODO
- [x] Display incoming UDP data
- [x] Add support for websocket subscription
- [x] Implement minimize to tray/status bar usage to display temperature
- [ ] Add measurement selection
- [x] Add derived measurements (Already added some)
- [ ] GUI configuration editor
- [x] Auto hide irrelevant sections
- [ ] Add display of UDP datagram history
- [ ] Plot data over time
- [x] Add support for multiple devices and hubs
- [ ] BLE Subscription?
