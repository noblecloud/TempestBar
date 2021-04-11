# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'udp.ui'
##
## Created by: Qt User Interface Compiler version 6.0.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_udp(object):
    def setupUi(self, udp):
        if not udp.objectName():
            udp.setObjectName(u"udp")
        udp.resize(1312, 560)
        self.gridLayout = QGridLayout(udp)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(10)
        self.gridLayout.setVerticalSpacing(0)
        self.gridLayout.setContentsMargins(-1, -1, 12, 0)
        self.skyGroup = QGroupBox(udp)
        self.skyGroup.setObjectName(u"skyGroup")
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.skyGroup.sizePolicy().hasHeightForWidth())
        self.skyGroup.setSizePolicy(sizePolicy)
        self.skyGroup.setMinimumSize(QSize(300, 0))
        self.skyGroup.setMaximumSize(QSize(300, 16777215))
        font = QFont()
        font.setPointSize(34)
        self.skyGroup.setFont(font)
        self.gridLayout_2 = QGridLayout(self.skyGroup)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.lightning = QGroupBox(self.skyGroup)
        self.lightning.setObjectName(u"lightning")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lightning.sizePolicy().hasHeightForWidth())
        self.lightning.setSizePolicy(sizePolicy1)
        font1 = QFont()
        font1.setPointSize(26)
        font1.setBold(True)
        self.lightning.setFont(font1)
        self.lightning.setFlat(True)
        self.lightning.setCheckable(False)
        self.lastStrikeLabel = QLabel(self.lightning)
        self.lastStrikeLabel.setObjectName(u"lastStrikeLabel")
        self.lastStrikeLabel.setGeometry(QRect(3, 41, 108, 29))
        font2 = QFont()
        font2.setPointSize(24)
        font2.setBold(False)
        self.lastStrikeLabel.setFont(font2)
        self.lastStrike = QLabel(self.lightning)
        self.lastStrike.setObjectName(u"lastStrike")
        self.lastStrike.setGeometry(QRect(119, 41, 16, 28))
        self.lastStrike.setFont(font2)
        self.strikeDistanceLabel = QLabel(self.lightning)
        self.strikeDistanceLabel.setObjectName(u"strikeDistanceLabel")
        self.strikeDistanceLabel.setGeometry(QRect(3, 78, 98, 29))
        self.strikeDistanceLabel.setFont(font2)
        self.strikeDistance = QLabel(self.lightning)
        self.strikeDistance.setObjectName(u"strikeDistance")
        self.strikeDistance.setGeometry(QRect(119, 78, 16, 28))
        self.strikeDistance.setFont(font2)
        self.strikeEnergyLabel = QLabel(self.lightning)
        self.strikeEnergyLabel.setObjectName(u"strikeEnergyLabel")
        self.strikeEnergyLabel.setGeometry(QRect(3, 115, 78, 29))
        self.strikeEnergyLabel.setFont(font2)
        self.strikeEnergy = QLabel(self.lightning)
        self.strikeEnergy.setObjectName(u"strikeEnergy")
        self.strikeEnergy.setGeometry(QRect(119, 115, 148, 29))
        self.strikeEnergy.setFont(font2)
        self.strikeTotalLabel = QLabel(self.lightning)
        self.strikeTotalLabel.setObjectName(u"strikeTotalLabel")
        self.strikeTotalLabel.setGeometry(QRect(3, 152, 56, 29))
        self.strikeTotalLabel.setFont(font2)
        self.strikeTotal = QLabel(self.lightning)
        self.strikeTotal.setObjectName(u"strikeTotal")
        self.strikeTotal.setGeometry(QRect(119, 152, 16, 28))
        self.strikeTotal.setFont(font2)

        self.gridLayout_2.addWidget(self.lightning, 1, 0, 1, 1)

        self.precipitation = QGroupBox(self.skyGroup)
        self.precipitation.setObjectName(u"precipitation")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.precipitation.sizePolicy().hasHeightForWidth())
        self.precipitation.setSizePolicy(sizePolicy2)
        self.precipitation.setFont(font1)
        self.precipitation.setFlat(True)
        self.precipitation.setCheckable(False)
        self.formLayout_6 = QFormLayout(self.precipitation)
        self.formLayout_6.setObjectName(u"formLayout_6")
        self.formLayout_6.setFieldGrowthPolicy(QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_6.setLabelAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.formLayout_6.setHorizontalSpacing(-1)
        self.formLayout_6.setVerticalSpacing(-1)
        self.formLayout_6.setContentsMargins(0, -1, 0, -1)
        self.rateLabel = QLabel(self.precipitation)
        self.rateLabel.setObjectName(u"rateLabel")
        self.rateLabel.setFont(font2)

        self.formLayout_6.setWidget(0, QFormLayout.LabelRole, self.rateLabel)

        self.rate = QLabel(self.precipitation)
        self.rate.setObjectName(u"rate")
        self.rate.setFont(font2)

        self.formLayout_6.setWidget(0, QFormLayout.FieldRole, self.rate)

        self.rateDescription = QLabel(self.precipitation)
        self.rateDescription.setObjectName(u"rateDescription")
        self.rateDescription.setFont(font2)

        self.formLayout_6.setWidget(1, QFormLayout.FieldRole, self.rateDescription)

        self.accumulationLabel = QLabel(self.precipitation)
        self.accumulationLabel.setObjectName(u"accumulationLabel")
        self.accumulationLabel.setFont(font2)

        self.formLayout_6.setWidget(2, QFormLayout.LabelRole, self.accumulationLabel)

        self.accumulation = QLabel(self.precipitation)
        self.accumulation.setObjectName(u"accumulation")
        self.accumulation.setFont(font2)

        self.formLayout_6.setWidget(2, QFormLayout.FieldRole, self.accumulation)


        self.gridLayout_2.addWidget(self.precipitation, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.skyGroup, 0, 3, 1, 1)

        self.solarGroup = QGroupBox(udp)
        self.solarGroup.setObjectName(u"solarGroup")
        self.solarGroup.setMinimumSize(QSize(320, 0))
        self.solarGroup.setMaximumSize(QSize(320, 16777215))
        self.solarGroup.setFont(font)
        self.solarGridLayout = QGridLayout(self.solarGroup)
        self.solarGridLayout.setObjectName(u"solarGridLayout")
        self.uv = QLabel(self.solarGroup)
        self.uv.setObjectName(u"uv")
        font3 = QFont()
        font3.setPointSize(24)
        self.uv.setFont(font3)

        self.solarGridLayout.addWidget(self.uv, 2, 1, 1, 1)

        self.irradianceLabel = QLabel(self.solarGroup)
        self.irradianceLabel.setObjectName(u"irradianceLabel")
        self.irradianceLabel.setFont(font3)

        self.solarGridLayout.addWidget(self.irradianceLabel, 1, 0, 1, 1)

        self.irradiance = QLabel(self.solarGroup)
        self.irradiance.setObjectName(u"irradiance")
        self.irradiance.setFont(font3)

        self.solarGridLayout.addWidget(self.irradiance, 1, 1, 1, 1)

        self.illuminance = QLabel(self.solarGroup)
        self.illuminance.setObjectName(u"illuminance")
        self.illuminance.setFont(font3)

        self.solarGridLayout.addWidget(self.illuminance, 0, 1, 1, 1)

        self.illuminanceLabel = QLabel(self.solarGroup)
        self.illuminanceLabel.setObjectName(u"illuminanceLabel")
        self.illuminanceLabel.setFont(font3)

        self.solarGridLayout.addWidget(self.illuminanceLabel, 0, 0, 1, 1)

        self.uvLabel = QLabel(self.solarGroup)
        self.uvLabel.setObjectName(u"uvLabel")
        self.uvLabel.setFont(font3)

        self.solarGridLayout.addWidget(self.uvLabel, 2, 0, 1, 1)

        self.solarSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.solarGridLayout.addItem(self.solarSpacer, 3, 0, 1, 1)


        self.gridLayout.addWidget(self.solarGroup, 0, 2, 1, 1)

        self.windGroup = QGroupBox(udp)
        self.windGroup.setObjectName(u"windGroup")
        self.windGroup.setMinimumSize(QSize(320, 0))
        self.windGroup.setMaximumSize(QSize(320, 16777215))
        self.windGroup.setFont(font)
        self.gridLayout_3 = QGridLayout(self.windGroup)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.windNow = QGroupBox(self.windGroup)
        self.windNow.setObjectName(u"windNow")
        sizePolicy2.setHeightForWidth(self.windNow.sizePolicy().hasHeightForWidth())
        self.windNow.setSizePolicy(sizePolicy2)
        self.windNow.setFont(font1)
        self.windNow.setFlat(True)
        self.windNow.setCheckable(False)
        self.formLayout = QFormLayout(self.windNow)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setFieldGrowthPolicy(QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setLabelAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.formLayout.setHorizontalSpacing(-1)
        self.formLayout.setVerticalSpacing(-1)
        self.formLayout.setContentsMargins(0, -1, 0, -1)
        self.windLabel = QLabel(self.windNow)
        self.windLabel.setObjectName(u"windLabel")
        self.windLabel.setFont(font2)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.windLabel)

        self.wind = QLabel(self.windNow)
        self.wind.setObjectName(u"wind")
        self.wind.setFont(font2)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.wind)

        self.windDirectionLabel = QLabel(self.windNow)
        self.windDirectionLabel.setObjectName(u"windDirectionLabel")
        self.windDirectionLabel.setFont(font2)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.windDirectionLabel)

        self.windDirection = QLabel(self.windNow)
        self.windDirection.setObjectName(u"windDirection")
        self.windDirection.setFont(font2)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.windDirection)


        self.gridLayout_3.addWidget(self.windNow, 0, 0, 1, 1)

        self.windAverages = QGroupBox(self.windGroup)
        self.windAverages.setObjectName(u"windAverages")
        self.windAverages.setFont(font1)
        self.windAverages.setFlat(True)
        self.formLayout_2 = QFormLayout(self.windAverages)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setFieldGrowthPolicy(QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_2.setLabelAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.formLayout_2.setContentsMargins(0, -1, -1, -1)
        self.lullLabel = QLabel(self.windAverages)
        self.lullLabel.setObjectName(u"lullLabel")
        self.lullLabel.setFont(font2)

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.lullLabel)

        self.lull = QLabel(self.windAverages)
        self.lull.setObjectName(u"lull")
        self.lull.setFont(font2)

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.lull)

        self.gustLabel = QLabel(self.windAverages)
        self.gustLabel.setObjectName(u"gustLabel")
        self.gustLabel.setFont(font2)

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.gustLabel)

        self.gust = QLabel(self.windAverages)
        self.gust.setObjectName(u"gust")
        self.gust.setFont(font2)

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.gust)

        self.windAverageLabel = QLabel(self.windAverages)
        self.windAverageLabel.setObjectName(u"windAverageLabel")
        self.windAverageLabel.setFont(font2)

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.windAverageLabel)

        self.windAverage = QLabel(self.windAverages)
        self.windAverage.setObjectName(u"windAverage")
        self.windAverage.setFont(font2)

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.windAverage)

        self.windDirectionAverageLabel = QLabel(self.windAverages)
        self.windDirectionAverageLabel.setObjectName(u"windDirectionAverageLabel")
        self.windDirectionAverageLabel.setFont(font2)

        self.formLayout_2.setWidget(3, QFormLayout.LabelRole, self.windDirectionAverageLabel)

        self.windDirectionAverage = QLabel(self.windAverages)
        self.windDirectionAverage.setObjectName(u"windDirectionAverage")
        self.windDirectionAverage.setFont(font2)

        self.formLayout_2.setWidget(3, QFormLayout.FieldRole, self.windDirectionAverage)


        self.gridLayout_3.addWidget(self.windAverages, 1, 0, 1, 1)

        self.windSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.windSpacer, 2, 0, 1, 1)


        self.gridLayout.addWidget(self.windGroup, 0, 1, 1, 1)

        self.airGroup = QGroupBox(udp)
        self.airGroup.setObjectName(u"airGroup")
        self.airGroup.setMinimumSize(QSize(300, 0))
        self.airGroup.setMaximumSize(QSize(300, 16777215))
        font4 = QFont()
        font4.setPointSize(34)
        font4.setBold(False)
        self.airGroup.setFont(font4)
        self.formLayout_3 = QFormLayout(self.airGroup)
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.formLayout_3.setFieldGrowthPolicy(QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_3.setLabelAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.temperatureLabel = QLabel(self.airGroup)
        self.temperatureLabel.setObjectName(u"temperatureLabel")
        self.temperatureLabel.setFont(font2)

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.temperatureLabel)

        self.temperature = QLabel(self.airGroup)
        self.temperature.setObjectName(u"temperature")
        self.temperature.setFont(font2)

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.temperature)

        self.humidityLabel = QLabel(self.airGroup)
        self.humidityLabel.setObjectName(u"humidityLabel")
        self.humidityLabel.setFont(font2)

        self.formLayout_3.setWidget(1, QFormLayout.LabelRole, self.humidityLabel)

        self.humidity = QLabel(self.airGroup)
        self.humidity.setObjectName(u"humidity")
        self.humidity.setFont(font2)

        self.formLayout_3.setWidget(1, QFormLayout.FieldRole, self.humidity)

        self.feelsLikeLabel = QLabel(self.airGroup)
        self.feelsLikeLabel.setObjectName(u"feelsLikeLabel")
        self.feelsLikeLabel.setFont(font2)

        self.formLayout_3.setWidget(2, QFormLayout.LabelRole, self.feelsLikeLabel)

        self.feelsLike = QLabel(self.airGroup)
        self.feelsLike.setObjectName(u"feelsLike")
        self.feelsLike.setFont(font2)

        self.formLayout_3.setWidget(2, QFormLayout.FieldRole, self.feelsLike)

        self.dewpointLabel = QLabel(self.airGroup)
        self.dewpointLabel.setObjectName(u"dewpointLabel")
        self.dewpointLabel.setFont(font2)

        self.formLayout_3.setWidget(3, QFormLayout.LabelRole, self.dewpointLabel)

        self.dewpoint = QLabel(self.airGroup)
        self.dewpoint.setObjectName(u"dewpoint")
        self.dewpoint.setFont(font2)

        self.formLayout_3.setWidget(3, QFormLayout.FieldRole, self.dewpoint)

        self.airDensityLabel = QLabel(self.airGroup)
        self.airDensityLabel.setObjectName(u"airDensityLabel")
        self.airDensityLabel.setFont(font2)

        self.formLayout_3.setWidget(4, QFormLayout.LabelRole, self.airDensityLabel)

        self.airDensity = QLabel(self.airGroup)
        self.airDensity.setObjectName(u"airDensity")
        self.airDensity.setFont(font2)

        self.formLayout_3.setWidget(4, QFormLayout.FieldRole, self.airDensity)

        self.pressureLabel = QLabel(self.airGroup)
        self.pressureLabel.setObjectName(u"pressureLabel")
        self.pressureLabel.setFont(font2)

        self.formLayout_3.setWidget(5, QFormLayout.LabelRole, self.pressureLabel)

        self.pressure = QLabel(self.airGroup)
        self.pressure.setObjectName(u"pressure")
        self.pressure.setFont(font2)

        self.formLayout_3.setWidget(5, QFormLayout.FieldRole, self.pressure)

        self.airSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.formLayout_3.setItem(6, QFormLayout.LabelRole, self.airSpacer)


        self.gridLayout.addWidget(self.airGroup, 0, 0, 1, 1)


        self.retranslateUi(udp)

        QMetaObject.connectSlotsByName(udp)
    # setupUi

    def retranslateUi(self, udp):
        udp.setWindowTitle(QCoreApplication.translate("udp", u"Form", None))
        self.skyGroup.setTitle(QCoreApplication.translate("udp", u"Sky", None))
        self.lightning.setTitle(QCoreApplication.translate("udp", u"Lightning", None))
        self.lastStrikeLabel.setText(QCoreApplication.translate("udp", u"Last Srike:", None))
        self.lastStrike.setText("")
        self.lastStrike.setProperty("measurement", QCoreApplication.translate("udp", u"wind", None))
        self.strikeDistanceLabel.setText(QCoreApplication.translate("udp", u"Distance:", None))
        self.strikeDistance.setText("")
        self.strikeDistance.setProperty("measurement", QCoreApplication.translate("udp", u"windDirection", None))
        self.strikeEnergyLabel.setText(QCoreApplication.translate("udp", u"Energy:", None))
        self.strikeEnergy.setText("")
        self.strikeEnergy.setProperty("measurement", QCoreApplication.translate("udp", u"windDirection", None))
        self.strikeTotalLabel.setText(QCoreApplication.translate("udp", u"Total:", None))
        self.strikeTotal.setText("")
        self.strikeTotal.setProperty("measurement", QCoreApplication.translate("udp", u"windDirection", None))
        self.precipitation.setTitle(QCoreApplication.translate("udp", u"Precipitation", None))
        self.rateLabel.setText(QCoreApplication.translate("udp", u"Rate:", None))
        self.rate.setText("")
        self.rate.setProperty("measurement", QCoreApplication.translate("udp", u"wind", None))
        self.rateDescription.setText("")
        self.rateDescription.setProperty("measurement", QCoreApplication.translate("udp", u"wind", None))
        self.accumulationLabel.setText(QCoreApplication.translate("udp", u"Accum:", None))
        self.accumulation.setText("")
        self.accumulation.setProperty("measurement", QCoreApplication.translate("udp", u"windDirection", None))
        self.solarGroup.setTitle(QCoreApplication.translate("udp", u"Solar", None))
        self.uv.setText("")
        self.uv.setProperty("measurement", "")
        self.irradianceLabel.setText(QCoreApplication.translate("udp", u"Solar Radiation:", None))
        self.irradiance.setText("")
        self.irradiance.setProperty("measurement", "")
        self.illuminance.setText("")
        self.illuminance.setProperty("measurement", "")
        self.illuminanceLabel.setText(QCoreApplication.translate("udp", u"Illuminance:", None))
        self.uvLabel.setText(QCoreApplication.translate("udp", u"UV:", None))
        self.windGroup.setTitle(QCoreApplication.translate("udp", u"Wind", None))
        self.windNow.setTitle(QCoreApplication.translate("udp", u"Now", None))
        self.windLabel.setText(QCoreApplication.translate("udp", u"Speed:", None))
        self.wind.setText("")
        self.wind.setProperty("measurement", QCoreApplication.translate("udp", u"wind", None))
        self.windDirectionLabel.setText(QCoreApplication.translate("udp", u"Direction:", None))
        self.windDirection.setText("")
        self.windDirection.setProperty("measurement", QCoreApplication.translate("udp", u"windDirection", None))
        self.windAverages.setTitle(QCoreApplication.translate("udp", u"Averages", None))
        self.lullLabel.setText(QCoreApplication.translate("udp", u"Lull:", None))
        self.lull.setText("")
        self.lull.setProperty("measurement", QCoreApplication.translate("udp", u"lullSpeed", None))
        self.gustLabel.setText(QCoreApplication.translate("udp", u"Gust:", None))
        self.gust.setText("")
        self.gust.setProperty("measurement", QCoreApplication.translate("udp", u"gustSpeed", None))
        self.windAverageLabel.setText(QCoreApplication.translate("udp", u"Speed", None))
        self.windAverage.setText("")
        self.windAverage.setProperty("measurement", QCoreApplication.translate("udp", u"windAverage", None))
        self.windDirectionAverageLabel.setText(QCoreApplication.translate("udp", u"Direction:", None))
        self.windDirectionAverage.setText("")
        self.windDirectionAverage.setProperty("measurement", QCoreApplication.translate("udp", u"windDirection", None))
        self.airGroup.setTitle(QCoreApplication.translate("udp", u"Air", None))
        self.temperatureLabel.setText(QCoreApplication.translate("udp", u"Temperature:", None))
        self.temperature.setText(QCoreApplication.translate("udp", u"0", None))
        self.temperature.setProperty("measurement", QCoreApplication.translate("udp", u"temperature", None))
        self.humidityLabel.setText(QCoreApplication.translate("udp", u"Humidity:", None))
        self.humidity.setText(QCoreApplication.translate("udp", u"0", None))
        self.humidity.setProperty("measurement", QCoreApplication.translate("udp", u"humidity", None))
        self.feelsLikeLabel.setText(QCoreApplication.translate("udp", u"Feels Like:", None))
        self.feelsLike.setText(QCoreApplication.translate("udp", u"0", None))
        self.feelsLike.setProperty("measurement", QCoreApplication.translate("udp", u"temperature", None))
        self.dewpointLabel.setText(QCoreApplication.translate("udp", u"Dew Point:", None))
        self.dewpoint.setText(QCoreApplication.translate("udp", u"0", None))
        self.dewpoint.setProperty("measurement", QCoreApplication.translate("udp", u"temperature", None))
        self.airDensityLabel.setText(QCoreApplication.translate("udp", u"Air Density:", None))
        self.airDensity.setText(QCoreApplication.translate("udp", u"0", None))
        self.airDensity.setProperty("measurement", QCoreApplication.translate("udp", u"pressure", None))
        self.pressureLabel.setText(QCoreApplication.translate("udp", u"Pressure:", None))
        self.pressure.setText(QCoreApplication.translate("udp", u"0", None))
        self.pressure.setProperty("measurement", QCoreApplication.translate("udp", u"pressure", None))
    # retranslateUi

