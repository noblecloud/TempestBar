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
        MainWindow.resize(1029, 429)
        MainWindow.setWindowTitle(u"WeatherFlowUDP")
        self.actionTest = QAction(MainWindow)
        self.actionTest.setObjectName(u"actionTest")
        self.actiontest = QAction(MainWindow)
        self.actiontest.setObjectName(u"actiontest")
        self.actionConfig = QAction(MainWindow)
        self.actionConfig.setObjectName(u"actionConfig")
        self.actionStatus = QAction(MainWindow)
        self.actionStatus.setObjectName(u"actionStatus")
        self.actionConfig_2 = QAction(MainWindow)
        self.actionConfig_2.setObjectName(u"actionConfig_2")
        self.actionUDP = QAction(MainWindow)
        self.actionUDP.setObjectName(u"actionUDP")
        self.actionWebsocket = QAction(MainWindow)
        self.actionWebsocket.setObjectName(u"actionWebsocket")
        self.actionLogin = QAction(MainWindow)
        self.actionLogin.setObjectName(u"actionLogin")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.airGroup = QGroupBox(self.centralwidget)
        self.airGroup.setObjectName(u"airGroup")
        font = QFont()
        font.setPointSize(34)
        font.setBold(False)
        self.airGroup.setFont(font)
        self.airGridLayout = QGridLayout(self.airGroup)
        self.airGridLayout.setObjectName(u"airGridLayout")
        self.temperatureLabel = QLabel(self.airGroup)
        self.temperatureLabel.setObjectName(u"temperatureLabel")
        font1 = QFont()
        font1.setPointSize(24)
        font1.setBold(False)
        self.temperatureLabel.setFont(font1)

        self.airGridLayout.addWidget(self.temperatureLabel, 0, 0, 1, 1)

        self.pressure = QLabel(self.airGroup)
        self.pressure.setObjectName(u"pressure")
        self.pressure.setFont(font1)

        self.airGridLayout.addWidget(self.pressure, 2, 1, 1, 1)

        self.pressureLabel = QLabel(self.airGroup)
        self.pressureLabel.setObjectName(u"pressureLabel")
        self.pressureLabel.setFont(font1)

        self.airGridLayout.addWidget(self.pressureLabel, 2, 0, 1, 1)

        self.temperature = QLabel(self.airGroup)
        self.temperature.setObjectName(u"temperature")
        self.temperature.setFont(font1)

        self.airGridLayout.addWidget(self.temperature, 0, 1, 1, 1)

        self.humidityLabel = QLabel(self.airGroup)
        self.humidityLabel.setObjectName(u"humidityLabel")
        self.humidityLabel.setFont(font1)

        self.airGridLayout.addWidget(self.humidityLabel, 1, 0, 1, 1)

        self.humidity = QLabel(self.airGroup)
        self.humidity.setObjectName(u"humidity")
        self.humidity.setFont(font1)

        self.airGridLayout.addWidget(self.humidity, 1, 1, 1, 1)


        self.horizontalLayout.addWidget(self.airGroup)

        self.windGroup = QGroupBox(self.centralwidget)
        self.windGroup.setObjectName(u"windGroup")
        font2 = QFont()
        font2.setPointSize(34)
        self.windGroup.setFont(font2)
        self.windGridLayout = QGridLayout(self.windGroup)
        self.windGridLayout.setObjectName(u"windGridLayout")
        self.windAverageLabel = QLabel(self.windGroup)
        self.windAverageLabel.setObjectName(u"windAverageLabel")
        font3 = QFont()
        font3.setPointSize(24)
        self.windAverageLabel.setFont(font3)

        self.windGridLayout.addWidget(self.windAverageLabel, 3, 0, 1, 1)

        self.windAverage = QLabel(self.windGroup)
        self.windAverage.setObjectName(u"windAverage")
        self.windAverage.setFont(font3)

        self.windGridLayout.addWidget(self.windAverage, 3, 1, 1, 1)

        self.lullLabel = QLabel(self.windGroup)
        self.lullLabel.setObjectName(u"lullLabel")
        self.lullLabel.setFont(font3)

        self.windGridLayout.addWidget(self.lullLabel, 1, 0, 1, 1)

        self.lull = QLabel(self.windGroup)
        self.lull.setObjectName(u"lull")
        self.lull.setFont(font3)

        self.windGridLayout.addWidget(self.lull, 1, 1, 1, 1)

        self.gustLabel = QLabel(self.windGroup)
        self.gustLabel.setObjectName(u"gustLabel")
        self.gustLabel.setFont(font3)

        self.windGridLayout.addWidget(self.gustLabel, 2, 0, 1, 1)

        self.wind = QLabel(self.windGroup)
        self.wind.setObjectName(u"wind")
        self.wind.setFont(font3)

        self.windGridLayout.addWidget(self.wind, 0, 1, 1, 1)

        self.windLabel = QLabel(self.windGroup)
        self.windLabel.setObjectName(u"windLabel")
        self.windLabel.setFont(font3)

        self.windGridLayout.addWidget(self.windLabel, 0, 0, 1, 1)

        self.windDirectionLabel = QLabel(self.windGroup)
        self.windDirectionLabel.setObjectName(u"windDirectionLabel")
        self.windDirectionLabel.setFont(font3)

        self.windGridLayout.addWidget(self.windDirectionLabel, 4, 0, 1, 1)

        self.windDirection = QLabel(self.windGroup)
        self.windDirection.setObjectName(u"windDirection")
        self.windDirection.setFont(font3)

        self.windGridLayout.addWidget(self.windDirection, 4, 1, 1, 1)

        self.gust = QLabel(self.windGroup)
        self.gust.setObjectName(u"gust")
        self.gust.setFont(font3)

        self.windGridLayout.addWidget(self.gust, 2, 1, 1, 1)


        self.horizontalLayout.addWidget(self.windGroup)

        self.solarGroup = QGroupBox(self.centralwidget)
        self.solarGroup.setObjectName(u"solarGroup")
        self.solarGroup.setFont(font2)
        self.solarGridLayout = QGridLayout(self.solarGroup)
        self.solarGridLayout.setObjectName(u"solarGridLayout")
        self.illuminanceLabel = QLabel(self.solarGroup)
        self.illuminanceLabel.setObjectName(u"illuminanceLabel")
        self.illuminanceLabel.setFont(font3)

        self.solarGridLayout.addWidget(self.illuminanceLabel, 0, 0, 1, 1)

        self.illuminance = QLabel(self.solarGroup)
        self.illuminance.setObjectName(u"illuminance")
        self.illuminance.setFont(font3)

        self.solarGridLayout.addWidget(self.illuminance, 0, 1, 1, 1)

        self.irradianceLabel = QLabel(self.solarGroup)
        self.irradianceLabel.setObjectName(u"irradianceLabel")
        self.irradianceLabel.setFont(font3)

        self.solarGridLayout.addWidget(self.irradianceLabel, 1, 0, 1, 1)

        self.irradiance = QLabel(self.solarGroup)
        self.irradiance.setObjectName(u"irradiance")
        self.irradiance.setFont(font3)

        self.solarGridLayout.addWidget(self.irradiance, 1, 1, 1, 1)

        self.uvLabel = QLabel(self.solarGroup)
        self.uvLabel.setObjectName(u"uvLabel")
        self.uvLabel.setFont(font3)

        self.solarGridLayout.addWidget(self.uvLabel, 2, 0, 1, 1)

        self.uv = QLabel(self.solarGroup)
        self.uv.setObjectName(u"uv")
        self.uv.setFont(font3)

        self.solarGridLayout.addWidget(self.uv, 2, 1, 1, 1)


        self.horizontalLayout.addWidget(self.solarGroup)

        self.skyGroup = QGroupBox(self.centralwidget)
        self.skyGroup.setObjectName(u"skyGroup")
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.skyGroup.sizePolicy().hasHeightForWidth())
        self.skyGroup.setSizePolicy(sizePolicy)
        self.skyGroup.setFont(font2)
        self.stormGridLayout = QGridLayout(self.skyGroup)
        self.stormGridLayout.setObjectName(u"stormGridLayout")
        self.accumulationLabel = QLabel(self.skyGroup)
        self.accumulationLabel.setObjectName(u"accumulationLabel")
        self.accumulationLabel.setFont(font3)

        self.stormGridLayout.addWidget(self.accumulationLabel, 1, 0, 1, 1)

        self.strikes = QLabel(self.skyGroup)
        self.strikes.setObjectName(u"strikes")
        self.strikes.setFont(font3)

        self.stormGridLayout.addWidget(self.strikes, 2, 1, 1, 1)

        self.accumulation = QLabel(self.skyGroup)
        self.accumulation.setObjectName(u"accumulation")
        self.accumulation.setFont(font3)

        self.stormGridLayout.addWidget(self.accumulation, 1, 1, 1, 1)

        self.strikesLabel = QLabel(self.skyGroup)
        self.strikesLabel.setObjectName(u"strikesLabel")
        self.strikesLabel.setFont(font3)

        self.stormGridLayout.addWidget(self.strikesLabel, 2, 0, 1, 1)

        self.precipRateLabel = QLabel(self.skyGroup)
        self.precipRateLabel.setObjectName(u"precipRateLabel")
        self.precipRateLabel.setFont(font3)

        self.stormGridLayout.addWidget(self.precipRateLabel, 0, 0, 1, 1)

        self.precipRate = QLabel(self.skyGroup)
        self.precipRate.setObjectName(u"precipRate")
        self.precipRate.setFont(font3)

        self.stormGridLayout.addWidget(self.precipRate, 0, 1, 1, 1)

        self.strikeDistance = QLabel(self.skyGroup)
        self.strikeDistance.setObjectName(u"strikeDistance")
        self.strikeDistance.setFont(font3)

        self.stormGridLayout.addWidget(self.strikeDistance, 3, 1, 1, 1)

        self.strikeDistanceLabel = QLabel(self.skyGroup)
        self.strikeDistanceLabel.setObjectName(u"strikeDistanceLabel")
        self.strikeDistanceLabel.setFont(font3)

        self.stormGridLayout.addWidget(self.strikeDistanceLabel, 3, 0, 1, 1)


        self.horizontalLayout.addWidget(self.skyGroup)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1029, 24))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuProtocal = QMenu(self.menubar)
        self.menuProtocal.setObjectName(u"menuProtocal")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
#if QT_CONFIG(shortcut)
        self.accumulationLabel.setBuddy(self.accumulation)
        self.strikesLabel.setBuddy(self.strikes)
        self.precipRateLabel.setBuddy(self.precipRate)
        self.strikeDistanceLabel.setBuddy(self.strikeDistance)
#endif // QT_CONFIG(shortcut)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuProtocal.menuAction())
        self.menuFile.addAction(self.actionStatus)
        self.menuFile.addAction(self.actionConfig_2)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionLogin)
        self.menuProtocal.addAction(self.actionUDP)
        self.menuProtocal.addAction(self.actionWebsocket)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        self.actionTest.setText(QCoreApplication.translate("MainWindow", u"Test", None))
        self.actiontest.setText(QCoreApplication.translate("MainWindow", u"test", None))
        self.actionConfig.setText(QCoreApplication.translate("MainWindow", u"Protocal", None))
        self.actionStatus.setText(QCoreApplication.translate("MainWindow", u"Status", None))
        self.actionConfig_2.setText(QCoreApplication.translate("MainWindow", u"Config", None))
        self.actionUDP.setText(QCoreApplication.translate("MainWindow", u"UDP", None))
        self.actionWebsocket.setText(QCoreApplication.translate("MainWindow", u"Websocket", None))
        self.actionLogin.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.airGroup.setTitle(QCoreApplication.translate("MainWindow", u"Air", None))
        self.temperatureLabel.setText(QCoreApplication.translate("MainWindow", u"Temperature:", None))
        self.pressure.setText("")
        self.pressure.setProperty("measurement", QCoreApplication.translate("MainWindow", u"pressure", None))
        self.pressureLabel.setText(QCoreApplication.translate("MainWindow", u"Pressure:", None))
        self.temperature.setText("")
        self.temperature.setProperty("measurement", QCoreApplication.translate("MainWindow", u"temperature", None))
        self.humidityLabel.setText(QCoreApplication.translate("MainWindow", u"Humidity:", None))
        self.humidity.setText("")
        self.humidity.setProperty("measurement", QCoreApplication.translate("MainWindow", u"humidity", None))
        self.windGroup.setTitle(QCoreApplication.translate("MainWindow", u"Wind", None))
        self.windAverageLabel.setText(QCoreApplication.translate("MainWindow", u"Average:", None))
        self.windAverage.setText("")
        self.windAverage.setProperty("measurement", QCoreApplication.translate("MainWindow", u"windAverage", None))
        self.lullLabel.setText(QCoreApplication.translate("MainWindow", u"Lull:", None))
        self.lull.setText("")
        self.lull.setProperty("measurement", QCoreApplication.translate("MainWindow", u"lullSpeed", None))
        self.gustLabel.setText(QCoreApplication.translate("MainWindow", u"Gust:", None))
        self.wind.setText("")
        self.wind.setProperty("measurement", QCoreApplication.translate("MainWindow", u"wind", None))
        self.windLabel.setText(QCoreApplication.translate("MainWindow", u"Instant:", None))
        self.windDirectionLabel.setText(QCoreApplication.translate("MainWindow", u"Direction:", None))
        self.windDirection.setText("")
        self.windDirection.setProperty("measurement", QCoreApplication.translate("MainWindow", u"windDirection", None))
        self.gust.setText("")
        self.gust.setProperty("measurement", QCoreApplication.translate("MainWindow", u"gustSpeed", None))
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
        self.skyGroup.setTitle(QCoreApplication.translate("MainWindow", u"Sky", None))
        self.accumulationLabel.setText(QCoreApplication.translate("MainWindow", u"Accumulation", None))
        self.strikes.setText("")
        self.strikes.setProperty("measurement", QCoreApplication.translate("MainWindow", u"lightning", None))
        self.accumulation.setText("")
        self.strikesLabel.setText(QCoreApplication.translate("MainWindow", u"Strikes:", None))
        self.precipRateLabel.setText(QCoreApplication.translate("MainWindow", u"Precipitation Rate", None))
        self.precipRate.setText("")
        self.precipRate.setProperty("measurement", QCoreApplication.translate("MainWindow", u"precipitationHourlyRaw", None))
        self.strikeDistance.setText("")
        self.strikeDistance.setProperty("measurement", QCoreApplication.translate("MainWindow", u"lightningDistance", None))
        self.strikeDistanceLabel.setText(QCoreApplication.translate("MainWindow", u"Strike Distance:", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuProtocal.setTitle(QCoreApplication.translate("MainWindow", u"Protocal", None))
        pass
    # retranslateUi

