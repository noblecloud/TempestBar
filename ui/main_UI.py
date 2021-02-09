# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.0.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(896, 540)
        MainWindow.setWindowTitle(u"WeatherFlowUDP")
        self.actionTest = QAction(MainWindow)
        self.actionTest.setObjectName(u"actionTest")
        self.actiontest = QAction(MainWindow)
        self.actiontest.setObjectName(u"actiontest")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.mainGridLayout = QGridLayout(self.centralwidget)
        self.mainGridLayout.setObjectName(u"mainGridLayout")
        self.hubGroup = QGroupBox(self.centralwidget)
        self.hubGroup.setObjectName(u"hubGroup")
        font = QFont()
        font.setPointSize(34)
        self.hubGroup.setFont(font)
        self.hubGroupLayout = QGridLayout(self.hubGroup)
        self.hubGroupLayout.setObjectName(u"hubGroupLayout")
        self.hubFirmwareLabel = QLabel(self.hubGroup)
        self.hubFirmwareLabel.setObjectName(u"hubFirmwareLabel")
        font1 = QFont()
        font1.setPointSize(24)
        self.hubFirmwareLabel.setFont(font1)

        self.hubGroupLayout.addWidget(self.hubFirmwareLabel, 1, 0, 1, 1)

        self.hubUptime = QLabel(self.hubGroup)
        self.hubUptime.setObjectName(u"hubUptime")
        self.hubUptime.setFont(font1)

        self.hubGroupLayout.addWidget(self.hubUptime, 2, 1, 1, 1)

        self.hubSerialLabel = QLabel(self.hubGroup)
        self.hubSerialLabel.setObjectName(u"hubSerialLabel")
        self.hubSerialLabel.setFont(font1)

        self.hubGroupLayout.addWidget(self.hubSerialLabel, 0, 0, 1, 1)

        self.hubSerial = QLabel(self.hubGroup)
        self.hubSerial.setObjectName(u"hubSerial")
        self.hubSerial.setFont(font1)

        self.hubGroupLayout.addWidget(self.hubSerial, 0, 1, 1, 1)

        self.hubFirmware = QLabel(self.hubGroup)
        self.hubFirmware.setObjectName(u"hubFirmware")
        self.hubFirmware.setFont(font1)

        self.hubGroupLayout.addWidget(self.hubFirmware, 1, 1, 1, 1)

        self.hubUptimeLabel = QLabel(self.hubGroup)
        self.hubUptimeLabel.setObjectName(u"hubUptimeLabel")
        self.hubUptimeLabel.setFont(font1)

        self.hubGroupLayout.addWidget(self.hubUptimeLabel, 2, 0, 1, 1)


        self.mainGridLayout.addWidget(self.hubGroup, 1, 2, 1, 1)

        self.skyGroup = QGroupBox(self.centralwidget)
        self.skyGroup.setObjectName(u"skyGroup")
        self.skyGroup.setFont(font)
        self.stormGridLayout = QGridLayout(self.skyGroup)
        self.stormGridLayout.setObjectName(u"stormGridLayout")
        self.strikes = QLabel(self.skyGroup)
        self.strikes.setObjectName(u"strikes")
        self.strikes.setFont(font1)

        self.stormGridLayout.addWidget(self.strikes, 2, 1, 1, 1)

        self.strikesLabel = QLabel(self.skyGroup)
        self.strikesLabel.setObjectName(u"strikesLabel")
        self.strikesLabel.setFont(font1)

        self.stormGridLayout.addWidget(self.strikesLabel, 2, 0, 1, 1)

        self.precipRateLabel = QLabel(self.skyGroup)
        self.precipRateLabel.setObjectName(u"precipRateLabel")
        self.precipRateLabel.setFont(font1)

        self.stormGridLayout.addWidget(self.precipRateLabel, 0, 0, 1, 1)

        self.precipRate = QLabel(self.skyGroup)
        self.precipRate.setObjectName(u"precipRate")
        self.precipRate.setFont(font1)

        self.stormGridLayout.addWidget(self.precipRate, 0, 1, 1, 1)

        self.strikeDistance = QLabel(self.skyGroup)
        self.strikeDistance.setObjectName(u"strikeDistance")
        self.strikeDistance.setFont(font1)

        self.stormGridLayout.addWidget(self.strikeDistance, 3, 1, 1, 1)

        self.strikeDistanceLabel = QLabel(self.skyGroup)
        self.strikeDistanceLabel.setObjectName(u"strikeDistanceLabel")
        self.strikeDistanceLabel.setFont(font1)

        self.stormGridLayout.addWidget(self.strikeDistanceLabel, 3, 0, 1, 1)

        self.accumulationLabel = QLabel(self.skyGroup)
        self.accumulationLabel.setObjectName(u"accumulationLabel")
        self.accumulationLabel.setFont(font1)

        self.stormGridLayout.addWidget(self.accumulationLabel, 1, 0, 1, 1)

        self.accumulation = QLabel(self.skyGroup)
        self.accumulation.setObjectName(u"accumulation")
        self.accumulation.setFont(font1)

        self.stormGridLayout.addWidget(self.accumulation, 1, 1, 1, 1)


        self.mainGridLayout.addWidget(self.skyGroup, 0, 1, 1, 1)

        self.deviceGroup = QGroupBox(self.centralwidget)
        self.deviceGroup.setObjectName(u"deviceGroup")
        self.deviceGroup.setFont(font)
        self.deviceGridLayout = QGridLayout(self.deviceGroup)
        self.deviceGridLayout.setObjectName(u"deviceGridLayout")
        self.deviceSerial = QLabel(self.deviceGroup)
        self.deviceSerial.setObjectName(u"deviceSerial")
        self.deviceSerial.setFont(font1)

        self.deviceGridLayout.addWidget(self.deviceSerial, 0, 1, 1, 1)

        self.deviceFirmware = QLabel(self.deviceGroup)
        self.deviceFirmware.setObjectName(u"deviceFirmware")
        self.deviceFirmware.setFont(font1)

        self.deviceGridLayout.addWidget(self.deviceFirmware, 1, 1, 1, 1)

        self.deviceFirmwareLabel = QLabel(self.deviceGroup)
        self.deviceFirmwareLabel.setObjectName(u"deviceFirmwareLabel")
        self.deviceFirmwareLabel.setFont(font1)

        self.deviceGridLayout.addWidget(self.deviceFirmwareLabel, 1, 0, 1, 1)

        self.deviceSerialLabel = QLabel(self.deviceGroup)
        self.deviceSerialLabel.setObjectName(u"deviceSerialLabel")
        self.deviceSerialLabel.setFont(font1)

        self.deviceGridLayout.addWidget(self.deviceSerialLabel, 0, 0, 1, 1)

        self.deviceSensorsLabel = QLabel(self.deviceGroup)
        self.deviceSensorsLabel.setObjectName(u"deviceSensorsLabel")
        self.deviceSensorsLabel.setFont(font1)

        self.deviceGridLayout.addWidget(self.deviceSensorsLabel, 3, 0, 1, 1)

        self.deviceSensors = QLabel(self.deviceGroup)
        self.deviceSensors.setObjectName(u"deviceSensors")
        self.deviceSensors.setFont(font1)

        self.deviceGridLayout.addWidget(self.deviceSensors, 3, 1, 1, 1)

        self.deviceUptimeLabel = QLabel(self.deviceGroup)
        self.deviceUptimeLabel.setObjectName(u"deviceUptimeLabel")
        self.deviceUptimeLabel.setFont(font1)

        self.deviceGridLayout.addWidget(self.deviceUptimeLabel, 2, 0, 1, 1)

        self.deviceUptime = QLabel(self.deviceGroup)
        self.deviceUptime.setObjectName(u"deviceUptime")
        self.deviceUptime.setFont(font1)

        self.deviceGridLayout.addWidget(self.deviceUptime, 2, 1, 1, 1)

        self.deviceBatteryLabel = QLabel(self.deviceGroup)
        self.deviceBatteryLabel.setObjectName(u"deviceBatteryLabel")
        self.deviceBatteryLabel.setFont(font1)

        self.deviceGridLayout.addWidget(self.deviceBatteryLabel, 4, 0, 1, 1)

        self.deviceBattery = QLabel(self.deviceGroup)
        self.deviceBattery.setObjectName(u"deviceBattery")
        self.deviceBattery.setFont(font1)

        self.deviceGridLayout.addWidget(self.deviceBattery, 4, 1, 1, 1)


        self.mainGridLayout.addWidget(self.deviceGroup, 1, 1, 1, 1)

        self.windGroup = QGroupBox(self.centralwidget)
        self.windGroup.setObjectName(u"windGroup")
        self.windGroup.setFont(font)
        self.windGridLayout = QGridLayout(self.windGroup)
        self.windGridLayout.setObjectName(u"windGridLayout")
        self.windDirection = QLabel(self.windGroup)
        self.windDirection.setObjectName(u"windDirection")
        self.windDirection.setFont(font1)

        self.windGridLayout.addWidget(self.windDirection, 4, 1, 1, 1)

        self.windLabel = QLabel(self.windGroup)
        self.windLabel.setObjectName(u"windLabel")
        self.windLabel.setFont(font1)

        self.windGridLayout.addWidget(self.windLabel, 0, 0, 1, 1)

        self.windDirectionLabel = QLabel(self.windGroup)
        self.windDirectionLabel.setObjectName(u"windDirectionLabel")
        self.windDirectionLabel.setFont(font1)

        self.windGridLayout.addWidget(self.windDirectionLabel, 4, 0, 1, 1)

        self.gust = QLabel(self.windGroup)
        self.gust.setObjectName(u"gust")
        self.gust.setFont(font1)

        self.windGridLayout.addWidget(self.gust, 2, 1, 1, 1)

        self.lullLabel = QLabel(self.windGroup)
        self.lullLabel.setObjectName(u"lullLabel")
        self.lullLabel.setFont(font1)

        self.windGridLayout.addWidget(self.lullLabel, 1, 0, 1, 1)

        self.gustLabel = QLabel(self.windGroup)
        self.gustLabel.setObjectName(u"gustLabel")
        self.gustLabel.setFont(font1)

        self.windGridLayout.addWidget(self.gustLabel, 2, 0, 1, 1)

        self.wind = QLabel(self.windGroup)
        self.wind.setObjectName(u"wind")
        self.wind.setFont(font1)

        self.windGridLayout.addWidget(self.wind, 0, 1, 1, 1)

        self.lull = QLabel(self.windGroup)
        self.lull.setObjectName(u"lull")
        self.lull.setFont(font1)

        self.windGridLayout.addWidget(self.lull, 1, 1, 1, 1)

        self.windAverageLabel = QLabel(self.windGroup)
        self.windAverageLabel.setObjectName(u"windAverageLabel")
        self.windAverageLabel.setFont(font1)

        self.windGridLayout.addWidget(self.windAverageLabel, 3, 0, 1, 1)

        self.windAverage = QLabel(self.windGroup)
        self.windAverage.setObjectName(u"windAverage")
        self.windAverage.setFont(font1)

        self.windGridLayout.addWidget(self.windAverage, 3, 1, 1, 1)


        self.mainGridLayout.addWidget(self.windGroup, 1, 0, 1, 1)

        self.solarGroup = QGroupBox(self.centralwidget)
        self.solarGroup.setObjectName(u"solarGroup")
        self.solarGroup.setFont(font)
        self.solarGridLayout = QGridLayout(self.solarGroup)
        self.solarGridLayout.setObjectName(u"solarGridLayout")
        self.illuminanceLabel = QLabel(self.solarGroup)
        self.illuminanceLabel.setObjectName(u"illuminanceLabel")
        self.illuminanceLabel.setFont(font1)

        self.solarGridLayout.addWidget(self.illuminanceLabel, 0, 0, 1, 1)

        self.illuminance = QLabel(self.solarGroup)
        self.illuminance.setObjectName(u"illuminance")
        self.illuminance.setFont(font1)

        self.solarGridLayout.addWidget(self.illuminance, 0, 1, 1, 1)

        self.irradianceLabel = QLabel(self.solarGroup)
        self.irradianceLabel.setObjectName(u"irradianceLabel")
        self.irradianceLabel.setFont(font1)

        self.solarGridLayout.addWidget(self.irradianceLabel, 1, 0, 1, 1)

        self.irradiance = QLabel(self.solarGroup)
        self.irradiance.setObjectName(u"irradiance")
        self.irradiance.setFont(font1)

        self.solarGridLayout.addWidget(self.irradiance, 1, 1, 1, 1)

        self.uvLabel = QLabel(self.solarGroup)
        self.uvLabel.setObjectName(u"uvLabel")
        self.uvLabel.setFont(font1)

        self.solarGridLayout.addWidget(self.uvLabel, 2, 0, 1, 1)

        self.uv = QLabel(self.solarGroup)
        self.uv.setObjectName(u"uv")
        self.uv.setFont(font1)

        self.solarGridLayout.addWidget(self.uv, 2, 1, 1, 1)


        self.mainGridLayout.addWidget(self.solarGroup, 0, 2, 1, 1)

        self.airGroup = QGroupBox(self.centralwidget)
        self.airGroup.setObjectName(u"airGroup")
        font2 = QFont()
        font2.setPointSize(34)
        font2.setBold(False)
        self.airGroup.setFont(font2)
        self.airGridLayout = QGridLayout(self.airGroup)
        self.airGridLayout.setObjectName(u"airGridLayout")
        self.pressure = QLabel(self.airGroup)
        self.pressure.setObjectName(u"pressure")
        font3 = QFont()
        font3.setPointSize(24)
        font3.setBold(False)
        self.pressure.setFont(font3)

        self.airGridLayout.addWidget(self.pressure, 2, 1, 1, 1)

        self.humidityLabel = QLabel(self.airGroup)
        self.humidityLabel.setObjectName(u"humidityLabel")
        self.humidityLabel.setFont(font3)

        self.airGridLayout.addWidget(self.humidityLabel, 1, 0, 1, 1)

        self.pressureLabel = QLabel(self.airGroup)
        self.pressureLabel.setObjectName(u"pressureLabel")
        self.pressureLabel.setFont(font3)

        self.airGridLayout.addWidget(self.pressureLabel, 2, 0, 1, 1)

        self.temperature = QLabel(self.airGroup)
        self.temperature.setObjectName(u"temperature")
        self.temperature.setFont(font3)

        self.airGridLayout.addWidget(self.temperature, 0, 1, 1, 1)

        self.humidity = QLabel(self.airGroup)
        self.humidity.setObjectName(u"humidity")
        self.humidity.setFont(font3)

        self.airGridLayout.addWidget(self.humidity, 1, 1, 1, 1)

        self.temperatureLabel = QLabel(self.airGroup)
        self.temperatureLabel.setObjectName(u"temperatureLabel")
        self.temperatureLabel.setFont(font3)

        self.airGridLayout.addWidget(self.temperatureLabel, 0, 0, 1, 1)


        self.mainGridLayout.addWidget(self.airGroup, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 896, 24))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
#if QT_CONFIG(shortcut)
        self.strikesLabel.setBuddy(self.strikes)
        self.precipRateLabel.setBuddy(self.precipRate)
        self.strikeDistanceLabel.setBuddy(self.strikeDistance)
        self.accumulationLabel.setBuddy(self.accumulation)
#endif // QT_CONFIG(shortcut)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        self.actionTest.setText(QCoreApplication.translate("MainWindow", u"Test", None))
        self.actiontest.setText(QCoreApplication.translate("MainWindow", u"test", None))
        self.hubGroup.setTitle(QCoreApplication.translate("MainWindow", u"Hub Status", None))
        self.hubFirmwareLabel.setText(QCoreApplication.translate("MainWindow", u"Firmware:", None))
        self.hubUptime.setText("")
        self.hubUptime.setProperty("measurement", "")
        self.hubSerialLabel.setText(QCoreApplication.translate("MainWindow", u"Serial:", None))
        self.hubSerial.setText("")
        self.hubSerial.setProperty("measurement", "")
        self.hubFirmware.setText("")
        self.hubFirmware.setProperty("measurement", "")
        self.hubUptimeLabel.setText(QCoreApplication.translate("MainWindow", u"Uptime:", None))
        self.skyGroup.setTitle(QCoreApplication.translate("MainWindow", u"Sky", None))
        self.strikes.setText("")
        self.strikes.setProperty("measurement", QCoreApplication.translate("MainWindow", u"lightning", None))
        self.strikesLabel.setText(QCoreApplication.translate("MainWindow", u"Strikes:", None))
        self.precipRateLabel.setText(QCoreApplication.translate("MainWindow", u"Precipitation Rate", None))
        self.precipRate.setText("")
        self.precipRate.setProperty("measurement", QCoreApplication.translate("MainWindow", u"precipitationHourlyRaw", None))
        self.strikeDistance.setText("")
        self.strikeDistance.setProperty("measurement", QCoreApplication.translate("MainWindow", u"lightningDistance", None))
        self.strikeDistanceLabel.setText(QCoreApplication.translate("MainWindow", u"Strike Distance:", None))
        self.accumulationLabel.setText(QCoreApplication.translate("MainWindow", u"Accumulation", None))
        self.accumulation.setText("")
        self.deviceGroup.setTitle(QCoreApplication.translate("MainWindow", u"Device Status", None))
        self.deviceSerial.setText("")
        self.deviceSerial.setProperty("measurement", "")
        self.deviceFirmware.setText("")
        self.deviceFirmware.setProperty("measurement", "")
        self.deviceFirmwareLabel.setText(QCoreApplication.translate("MainWindow", u"Firmware:", None))
        self.deviceSerialLabel.setText(QCoreApplication.translate("MainWindow", u"Serial:", None))
        self.deviceSensorsLabel.setText(QCoreApplication.translate("MainWindow", u"Sensors:", None))
        self.deviceSensors.setText("")
        self.deviceSensors.setProperty("measurement", "")
        self.deviceUptimeLabel.setText(QCoreApplication.translate("MainWindow", u"Uptime:", None))
        self.deviceUptime.setText("")
        self.deviceUptime.setProperty("measurement", "")
        self.deviceBatteryLabel.setText(QCoreApplication.translate("MainWindow", u"Battery:", None))
        self.deviceBattery.setText("")
        self.deviceBattery.setProperty("measurement", "")
        self.windGroup.setTitle(QCoreApplication.translate("MainWindow", u"Wind", None))
        self.windDirection.setText("")
        self.windDirection.setProperty("measurement", QCoreApplication.translate("MainWindow", u"windDirection", None))
        self.windLabel.setText(QCoreApplication.translate("MainWindow", u"Instant:", None))
        self.windDirectionLabel.setText(QCoreApplication.translate("MainWindow", u"Direction:", None))
        self.gust.setText("")
        self.gust.setProperty("measurement", QCoreApplication.translate("MainWindow", u"gustSpeed", None))
        self.lullLabel.setText(QCoreApplication.translate("MainWindow", u"Lull:", None))
        self.gustLabel.setText(QCoreApplication.translate("MainWindow", u"Gust:", None))
        self.wind.setText("")
        self.wind.setProperty("measurement", QCoreApplication.translate("MainWindow", u"wind", None))
        self.lull.setText("")
        self.lull.setProperty("measurement", QCoreApplication.translate("MainWindow", u"lullSpeed", None))
        self.windAverageLabel.setText(QCoreApplication.translate("MainWindow", u"Average:", None))
        self.windAverage.setText("")
        self.windAverage.setProperty("measurement", QCoreApplication.translate("MainWindow", u"windAverage", None))
        self.solarGroup.setTitle(QCoreApplication.translate("MainWindow", u"Solar", None))
        self.illuminanceLabel.setText(QCoreApplication.translate("MainWindow", u"Illuminance:", None))
        self.illuminance.setText("")
        self.illuminance.setProperty("measurement", "")
        self.irradianceLabel.setText(QCoreApplication.translate("MainWindow", u"Solar Radiation:", None))
        self.irradiance.setText("")
        self.irradiance.setProperty("measurement", "")
        self.uvLabel.setText(QCoreApplication.translate("MainWindow", u"UV:", None))
        self.uv.setText("")
        self.uv.setProperty("measurement", "")
        self.airGroup.setTitle(QCoreApplication.translate("MainWindow", u"Air", None))
        self.pressure.setText("")
        self.pressure.setProperty("measurement", QCoreApplication.translate("MainWindow", u"pressure", None))
        self.humidityLabel.setText(QCoreApplication.translate("MainWindow", u"Humidity:", None))
        self.pressureLabel.setText(QCoreApplication.translate("MainWindow", u"Pressure:", None))
        self.temperature.setText("")
        self.temperature.setProperty("measurement", QCoreApplication.translate("MainWindow", u"temperature", None))
        self.humidity.setText("")
        self.humidity.setProperty("measurement", QCoreApplication.translate("MainWindow", u"humidity", None))
        self.temperatureLabel.setText(QCoreApplication.translate("MainWindow", u"Temperature:", None))
        pass
    # retranslateUi

