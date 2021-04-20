# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'websocket.ui'
##
## Created by: Qt User Interface Compiler version 6.0.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from ui.easyLabel import EasyLabel


class Ui_websocket(object):
    def setupUi(self, websocket):
        if not websocket.objectName():
            websocket.setObjectName(u"websocket")
        websocket.resize(950, 377)
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(websocket.sizePolicy().hasHeightForWidth())
        websocket.setSizePolicy(sizePolicy)
        websocket.setMinimumSize(QSize(630, 368))
        self.horizontalLayout = QHBoxLayout(websocket)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetMinimumSize)
        self.horizontalLayout.setContentsMargins(5, 0, 5, 0)
        self.airGroup = QGroupBox(websocket)
        self.airGroup.setObjectName(u"airGroup")
        self.airGroup.setMinimumSize(QSize(300, 0))
        self.airGroup.setMaximumSize(QSize(300, 16777215))
        font = QFont()
        font.setPointSize(34)
        font.setBold(False)
        self.airGroup.setFont(font)
        self.airGroup.setFlat(True)
        self.airGroup.setCheckable(False)
        self.formLayout_3 = QFormLayout(self.airGroup)
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.formLayout_3.setFieldGrowthPolicy(QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_3.setLabelAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.formLayout_3.setContentsMargins(-1, 7, -1, 0)
        self.temperatureLabel = QLabel(self.airGroup)
        self.temperatureLabel.setObjectName(u"temperatureLabel")
        font1 = QFont()
        font1.setPointSize(24)
        font1.setBold(False)
        self.temperatureLabel.setFont(font1)

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.temperatureLabel)

        self.temperature = EasyLabel(self.airGroup)
        self.temperature.setObjectName(u"temperature")
        self.temperature.setEnabled(False)
        self.temperature.setFont(font1)
        self.temperature.setProperty("showUnit", False)

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.temperature)

        self.humidityLabel = QLabel(self.airGroup)
        self.humidityLabel.setObjectName(u"humidityLabel")
        self.humidityLabel.setFont(font1)

        self.formLayout_3.setWidget(1, QFormLayout.LabelRole, self.humidityLabel)

        self.humidity = EasyLabel(self.airGroup)
        self.humidity.setObjectName(u"humidity")
        self.humidity.setEnabled(False)
        self.humidity.setFont(font1)
        self.humidity.setProperty("showUnit", False)

        self.formLayout_3.setWidget(1, QFormLayout.FieldRole, self.humidity)

        self.feelsLikeLabel = QLabel(self.airGroup)
        self.feelsLikeLabel.setObjectName(u"feelsLikeLabel")
        self.feelsLikeLabel.setFont(font1)

        self.formLayout_3.setWidget(2, QFormLayout.LabelRole, self.feelsLikeLabel)

        self.feelsLike = EasyLabel(self.airGroup)
        self.feelsLike.setObjectName(u"feelsLike")
        self.feelsLike.setEnabled(False)
        self.feelsLike.setFont(font1)
        self.feelsLike.setProperty("showUnit", False)

        self.formLayout_3.setWidget(2, QFormLayout.FieldRole, self.feelsLike)

        self.dewpointLabel = QLabel(self.airGroup)
        self.dewpointLabel.setObjectName(u"dewpointLabel")
        self.dewpointLabel.setFont(font1)

        self.formLayout_3.setWidget(3, QFormLayout.LabelRole, self.dewpointLabel)

        self.dewpoint = EasyLabel(self.airGroup)
        self.dewpoint.setObjectName(u"dewpoint")
        self.dewpoint.setEnabled(False)
        self.dewpoint.setFont(font1)
        self.dewpoint.setProperty("showUnit", False)

        self.formLayout_3.setWidget(3, QFormLayout.FieldRole, self.dewpoint)

        self.airDensityLabel = QLabel(self.airGroup)
        self.airDensityLabel.setObjectName(u"airDensityLabel")
        self.airDensityLabel.setFont(font1)

        self.formLayout_3.setWidget(4, QFormLayout.LabelRole, self.airDensityLabel)

        self.airDensity = EasyLabel(self.airGroup)
        self.airDensity.setObjectName(u"airDensity")
        self.airDensity.setEnabled(False)
        self.airDensity.setFont(font1)
        self.airDensity.setProperty("showUnit", True)

        self.formLayout_3.setWidget(4, QFormLayout.FieldRole, self.airDensity)

        self.pressureLabel = QLabel(self.airGroup)
        self.pressureLabel.setObjectName(u"pressureLabel")
        self.pressureLabel.setFont(font1)

        self.formLayout_3.setWidget(5, QFormLayout.LabelRole, self.pressureLabel)

        self.pressure = EasyLabel(self.airGroup)
        self.pressure.setObjectName(u"pressure")
        self.pressure.setEnabled(False)
        self.pressure.setFont(font1)
        self.pressure.setProperty("showUnit", True)

        self.formLayout_3.setWidget(5, QFormLayout.FieldRole, self.pressure)

        self.illuminanceLabel = QLabel(self.airGroup)
        self.illuminanceLabel.setObjectName(u"illuminanceLabel")
        self.illuminanceLabel.setFont(font1)

        self.formLayout_3.setWidget(6, QFormLayout.LabelRole, self.illuminanceLabel)

        self.illuminance = EasyLabel(self.airGroup)
        self.illuminance.setObjectName(u"illuminance")
        self.illuminance.setEnabled(False)
        self.illuminance.setFont(font1)
        self.illuminance.setProperty("showUnit", True)

        self.formLayout_3.setWidget(6, QFormLayout.FieldRole, self.illuminance)

        self.irradianceLabel = QLabel(self.airGroup)
        self.irradianceLabel.setObjectName(u"irradianceLabel")
        self.irradianceLabel.setFont(font1)

        self.formLayout_3.setWidget(7, QFormLayout.LabelRole, self.irradianceLabel)

        self.irradiance = EasyLabel(self.airGroup)
        self.irradiance.setObjectName(u"irradiance")
        self.irradiance.setEnabled(False)
        self.irradiance.setFont(font1)
        self.irradiance.setProperty("showUnit", True)

        self.formLayout_3.setWidget(7, QFormLayout.FieldRole, self.irradiance)

        self.uvLabel = QLabel(self.airGroup)
        self.uvLabel.setObjectName(u"uvLabel")
        self.uvLabel.setFont(font1)

        self.formLayout_3.setWidget(8, QFormLayout.LabelRole, self.uvLabel)

        self.uv = EasyLabel(self.airGroup)
        self.uv.setObjectName(u"uv")
        self.uv.setEnabled(False)
        self.uv.setFont(font1)
        self.uv.setProperty("showUnit", False)

        self.formLayout_3.setWidget(8, QFormLayout.FieldRole, self.uv)

        self.airSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.formLayout_3.setItem(9, QFormLayout.LabelRole, self.airSpacer)


        self.horizontalLayout.addWidget(self.airGroup)

        self.windGroup = QGroupBox(websocket)
        self.windGroup.setObjectName(u"windGroup")
        self.windGroup.setMinimumSize(QSize(320, 0))
        self.windGroup.setMaximumSize(QSize(320, 16777215))
        font2 = QFont()
        font2.setPointSize(34)
        self.windGroup.setFont(font2)
        self.windGroup.setFlat(True)
        self.gridLayout_3 = QGridLayout(self.windGroup)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(-1, 0, -1, 0)
        self.windNow = QGroupBox(self.windGroup)
        self.windNow.setObjectName(u"windNow")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.windNow.sizePolicy().hasHeightForWidth())
        self.windNow.setSizePolicy(sizePolicy1)
        font3 = QFont()
        font3.setPointSize(26)
        font3.setBold(True)
        self.windNow.setFont(font3)
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
        self.windLabel.setFont(font1)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.windLabel)

        self.wind = EasyLabel(self.windNow)
        self.wind.setObjectName(u"wind")
        self.wind.setEnabled(False)
        self.wind.setFont(font1)
        self.wind.setProperty("showUnit", True)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.wind)

        self.windDirectionLabel = QLabel(self.windNow)
        self.windDirectionLabel.setObjectName(u"windDirectionLabel")
        self.windDirectionLabel.setFont(font1)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.windDirectionLabel)

        self.windDirection = EasyLabel(self.windNow)
        self.windDirection.setObjectName(u"windDirection")
        self.windDirection.setEnabled(False)
        self.windDirection.setFont(font1)
        self.windDirection.setProperty("showUnit", False)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.windDirection)


        self.gridLayout_3.addWidget(self.windNow, 0, 0, 1, 1)

        self.windAverages = QGroupBox(self.windGroup)
        self.windAverages.setObjectName(u"windAverages")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.windAverages.sizePolicy().hasHeightForWidth())
        self.windAverages.setSizePolicy(sizePolicy2)
        self.windAverages.setFont(font3)
        self.windAverages.setFlat(True)
        self.formLayout_2 = QFormLayout(self.windAverages)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setFieldGrowthPolicy(QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_2.setLabelAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.formLayout_2.setContentsMargins(0, -1, -1, 0)
        self.lullLabel = QLabel(self.windAverages)
        self.lullLabel.setObjectName(u"lullLabel")
        self.lullLabel.setFont(font1)

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.lullLabel)

        self.lull = EasyLabel(self.windAverages)
        self.lull.setObjectName(u"lull")
        self.lull.setEnabled(False)
        self.lull.setFont(font1)
        self.lull.setProperty("showUnit", True)

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.lull)

        self.gustLabel = QLabel(self.windAverages)
        self.gustLabel.setObjectName(u"gustLabel")
        self.gustLabel.setFont(font1)

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.gustLabel)

        self.gust = EasyLabel(self.windAverages)
        self.gust.setObjectName(u"gust")
        self.gust.setEnabled(False)
        self.gust.setFont(font1)
        self.gust.setProperty("showUnit", True)

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.gust)

        self.windAverageLabel = QLabel(self.windAverages)
        self.windAverageLabel.setObjectName(u"windAverageLabel")
        self.windAverageLabel.setFont(font1)

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.windAverageLabel)

        self.windAverage = EasyLabel(self.windAverages)
        self.windAverage.setObjectName(u"windAverage")
        self.windAverage.setEnabled(False)
        self.windAverage.setFont(font1)
        self.windAverage.setProperty("showUnit", True)

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.windAverage)

        self.windDirectionAverageLabel = QLabel(self.windAverages)
        self.windDirectionAverageLabel.setObjectName(u"windDirectionAverageLabel")
        self.windDirectionAverageLabel.setFont(font1)

        self.formLayout_2.setWidget(3, QFormLayout.LabelRole, self.windDirectionAverageLabel)

        self.windDirectionAverage = EasyLabel(self.windAverages)
        self.windDirectionAverage.setObjectName(u"windDirectionAverage")
        self.windDirectionAverage.setEnabled(False)
        self.windDirectionAverage.setFont(font1)
        self.windDirectionAverage.setProperty("showUnit", False)

        self.formLayout_2.setWidget(3, QFormLayout.FieldRole, self.windDirectionAverage)


        self.gridLayout_3.addWidget(self.windAverages, 1, 0, 1, 1)

        self.windSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.windSpacer, 2, 0, 1, 1)


        self.horizontalLayout.addWidget(self.windGroup)

        self.skyGroup = QGroupBox(websocket)
        self.skyGroup.setObjectName(u"skyGroup")
        self.skyGroup.setMinimumSize(QSize(320, 0))
        self.skyGroup.setMaximumSize(QSize(320, 16777215))
        self.skyGroup.setFont(font2)
        self.skyGroup.setFlat(True)
        self.gridLayout_2 = QGridLayout(self.skyGroup)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setVerticalSpacing(-1)
        self.gridLayout_2.setContentsMargins(-1, 0, -1, 0)
        self.precipitation = QGroupBox(self.skyGroup)
        self.precipitation.setObjectName(u"precipitation")
        sizePolicy1.setHeightForWidth(self.precipitation.sizePolicy().hasHeightForWidth())
        self.precipitation.setSizePolicy(sizePolicy1)
        self.precipitation.setFont(font3)
        self.precipitation.setFlat(True)
        self.precipitation.setCheckable(False)
        self.formLayout_6 = QFormLayout(self.precipitation)
        self.formLayout_6.setObjectName(u"formLayout_6")
        self.formLayout_6.setFieldGrowthPolicy(QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_6.setLabelAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.formLayout_6.setContentsMargins(0, -1, 0, -1)
        self.rateLabel = QLabel(self.precipitation)
        self.rateLabel.setObjectName(u"rateLabel")
        self.rateLabel.setFont(font1)

        self.formLayout_6.setWidget(0, QFormLayout.LabelRole, self.rateLabel)

        self.rate = EasyLabel(self.precipitation)
        self.rate.setObjectName(u"rate")
        self.rate.setEnabled(False)
        self.rate.setFont(font1)
        self.rate.setProperty("showUnit", True)

        self.formLayout_6.setWidget(0, QFormLayout.FieldRole, self.rate)

        self.rateDescription = EasyLabel(self.precipitation)
        self.rateDescription.setObjectName(u"rateDescription")
        self.rateDescription.setEnabled(False)
        self.rateDescription.setFont(font1)
        self.rateDescription.setProperty("showUnit", False)

        self.formLayout_6.setWidget(1, QFormLayout.FieldRole, self.rateDescription)

        self.accumulationLabel = QLabel(self.precipitation)
        self.accumulationLabel.setObjectName(u"accumulationLabel")
        self.accumulationLabel.setFont(font1)

        self.formLayout_6.setWidget(2, QFormLayout.LabelRole, self.accumulationLabel)

        self.accumulation = EasyLabel(self.precipitation)
        self.accumulation.setObjectName(u"accumulation")
        self.accumulation.setEnabled(False)
        self.accumulation.setFont(font1)
        self.accumulation.setProperty("showUnit", True)

        self.formLayout_6.setWidget(2, QFormLayout.FieldRole, self.accumulation)


        self.gridLayout_2.addWidget(self.precipitation, 0, 0, 1, 1)

        self.lightning = QGroupBox(self.skyGroup)
        self.lightning.setObjectName(u"lightning")
        sizePolicy2.setHeightForWidth(self.lightning.sizePolicy().hasHeightForWidth())
        self.lightning.setSizePolicy(sizePolicy2)
        self.lightning.setFont(font3)
        self.lightning.setFlat(True)
        self.lightning.setCheckable(False)
        self.formLayout_4 = QFormLayout(self.lightning)
        self.formLayout_4.setObjectName(u"formLayout_4")
        self.formLayout_4.setSizeConstraint(QLayout.SetNoConstraint)
        self.formLayout_4.setFieldGrowthPolicy(QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_4.setLabelAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.formLayout_4.setContentsMargins(0, -1, 0, 0)
        self.lastStrikeLabel = QLabel(self.lightning)
        self.lastStrikeLabel.setObjectName(u"lastStrikeLabel")
        self.lastStrikeLabel.setFont(font1)

        self.formLayout_4.setWidget(0, QFormLayout.LabelRole, self.lastStrikeLabel)

        self.lastStrike = EasyLabel(self.lightning)
        self.lastStrike.setObjectName(u"lastStrike")
        self.lastStrike.setEnabled(False)
        self.lastStrike.setFont(font1)
        self.lastStrike.setProperty("showUnit", True)

        self.formLayout_4.setWidget(0, QFormLayout.FieldRole, self.lastStrike)

        self.strikeDistanceLabel = QLabel(self.lightning)
        self.strikeDistanceLabel.setObjectName(u"strikeDistanceLabel")
        self.strikeDistanceLabel.setFont(font1)

        self.formLayout_4.setWidget(1, QFormLayout.LabelRole, self.strikeDistanceLabel)

        self.strikeDistance = EasyLabel(self.lightning)
        self.strikeDistance.setObjectName(u"strikeDistance")
        self.strikeDistance.setEnabled(False)
        self.strikeDistance.setFont(font1)
        self.strikeDistance.setProperty("showUnit", True)

        self.formLayout_4.setWidget(1, QFormLayout.FieldRole, self.strikeDistance)

        self.strikeEnergyLabel = QLabel(self.lightning)
        self.strikeEnergyLabel.setObjectName(u"strikeEnergyLabel")
        self.strikeEnergyLabel.setFont(font1)

        self.formLayout_4.setWidget(2, QFormLayout.LabelRole, self.strikeEnergyLabel)

        self.strikeEnergy = EasyLabel(self.lightning)
        self.strikeEnergy.setObjectName(u"strikeEnergy")
        self.strikeEnergy.setEnabled(False)
        self.strikeEnergy.setFont(font1)
        self.strikeEnergy.setProperty("showUnit", False)

        self.formLayout_4.setWidget(2, QFormLayout.FieldRole, self.strikeEnergy)

        self.strikeTotalLabel = QLabel(self.lightning)
        self.strikeTotalLabel.setObjectName(u"strikeTotalLabel")
        self.strikeTotalLabel.setFont(font1)

        self.formLayout_4.setWidget(3, QFormLayout.LabelRole, self.strikeTotalLabel)

        self.strikeTotal = EasyLabel(self.lightning)
        self.strikeTotal.setObjectName(u"strikeTotal")
        self.strikeTotal.setEnabled(False)
        self.strikeTotal.setFont(font1)
        self.strikeTotal.setProperty("showUnit", False)

        self.formLayout_4.setWidget(3, QFormLayout.FieldRole, self.strikeTotal)


        self.gridLayout_2.addWidget(self.lightning, 1, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer, 2, 0, 1, 1)


        self.horizontalLayout.addWidget(self.skyGroup)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 1)

        self.retranslateUi(websocket)

        QMetaObject.connectSlotsByName(websocket)
    # setupUi

    def retranslateUi(self, websocket):
        websocket.setWindowTitle(QCoreApplication.translate("websocket", u"Form", None))
        self.airGroup.setTitle("")
        self.temperatureLabel.setText(QCoreApplication.translate("websocket", u"Temperature:", None))
        self.temperature.setText(QCoreApplication.translate("websocket", u"70\u00ba", None))
        self.temperature.setProperty("measurement", "")
        self.humidityLabel.setText(QCoreApplication.translate("websocket", u"Humidity:", None))
        self.humidity.setText(QCoreApplication.translate("websocket", u"75%", None))
        self.humidity.setProperty("measurement", QCoreApplication.translate("websocket", u"humidity", None))
        self.feelsLikeLabel.setText(QCoreApplication.translate("websocket", u"Feels Like:", None))
        self.feelsLike.setText(QCoreApplication.translate("websocket", u"70\u00ba", None))
        self.feelsLike.setProperty("measurement", QCoreApplication.translate("websocket", u"temperature", None))
        self.dewpointLabel.setText(QCoreApplication.translate("websocket", u"Dew Point:", None))
        self.dewpoint.setText(QCoreApplication.translate("websocket", u"59.2\u00ba", None))
        self.dewpoint.setProperty("measurement", QCoreApplication.translate("websocket", u"temperature", None))
        self.airDensityLabel.setText(QCoreApplication.translate("websocket", u"Air Density:", None))
        self.airDensity.setText(QCoreApplication.translate("websocket", u"1.18 oz/ft\u00b3", None))
        self.airDensity.setProperty("measurement", QCoreApplication.translate("websocket", u"pressure", None))
        self.pressureLabel.setText(QCoreApplication.translate("websocket", u"Pressure:", None))
        self.pressure.setText(QCoreApplication.translate("websocket", u"29.7 inHg", None))
        self.illuminanceLabel.setText(QCoreApplication.translate("websocket", u"Illuminance:", None))
        self.illuminance.setText(QCoreApplication.translate("websocket", u"91.2k lux", None))
        self.illuminance.setProperty("measurement", "")
        self.irradianceLabel.setText(QCoreApplication.translate("websocket", u"Radiation:", None))
        self.irradiance.setText(QCoreApplication.translate("websocket", u"858 W/m\u00b2", None))
        self.irradiance.setProperty("measurement", "")
        self.uvLabel.setText(QCoreApplication.translate("websocket", u"UV:", None))
        self.uv.setText(QCoreApplication.translate("websocket", u"5", None))
        self.uv.setProperty("measurement", "")
        self.windGroup.setTitle("")
        self.windNow.setTitle(QCoreApplication.translate("websocket", u"Now", None))
        self.windLabel.setText(QCoreApplication.translate("websocket", u"Speed:", None))
        self.wind.setText(QCoreApplication.translate("websocket", u"0 mph", None))
        self.wind.setProperty("measurement", QCoreApplication.translate("websocket", u"wind", None))
        self.windDirectionLabel.setText(QCoreApplication.translate("websocket", u"Direction:", None))
        self.windDirection.setText(QCoreApplication.translate("websocket", u"NE (39\u00ba)", None))
        self.windDirection.setProperty("measurement", QCoreApplication.translate("websocket", u"windDirection", None))
        self.windAverages.setTitle(QCoreApplication.translate("websocket", u"Average", None))
        self.lullLabel.setText(QCoreApplication.translate("websocket", u"Lull:", None))
        self.lull.setText(QCoreApplication.translate("websocket", u"0 mph", None))
        self.lull.setProperty("measurement", QCoreApplication.translate("websocket", u"lullSpeed", None))
        self.gustLabel.setText(QCoreApplication.translate("websocket", u"Gust:", None))
        self.gust.setText(QCoreApplication.translate("websocket", u"1.5 mph", None))
        self.gust.setProperty("measurement", QCoreApplication.translate("websocket", u"gustSpeed", None))
        self.windAverageLabel.setText(QCoreApplication.translate("websocket", u"Speed", None))
        self.windAverage.setText(QCoreApplication.translate("websocket", u"0.9 mph", None))
        self.windAverage.setProperty("measurement", QCoreApplication.translate("websocket", u"windAverage", None))
        self.windDirectionAverageLabel.setText(QCoreApplication.translate("websocket", u"Direction:", None))
        self.windDirectionAverage.setText(QCoreApplication.translate("websocket", u"NNE (22\u00ba)", None))
        self.windDirectionAverage.setProperty("measurement", QCoreApplication.translate("websocket", u"windDirection", None))
        self.skyGroup.setTitle("")
        self.precipitation.setTitle(QCoreApplication.translate("websocket", u"Precipitation", None))
        self.rateLabel.setText(QCoreApplication.translate("websocket", u"Rate:", None))
        self.rate.setText(QCoreApplication.translate("websocket", u"0 in/hr", None))
        self.rate.setProperty("measurement", QCoreApplication.translate("websocket", u"wind", None))
        self.rateDescription.setText(QCoreApplication.translate("websocket", u"None", None))
        self.rateDescription.setProperty("measurement", QCoreApplication.translate("websocket", u"wind", None))
        self.accumulationLabel.setText(QCoreApplication.translate("websocket", u"Total:", None))
        self.accumulation.setText(QCoreApplication.translate("websocket", u"0 in", None))
        self.accumulation.setProperty("measurement", QCoreApplication.translate("websocket", u"windDirection", None))
        self.lightning.setTitle(QCoreApplication.translate("websocket", u"Lightning", None))
        self.lastStrikeLabel.setText(QCoreApplication.translate("websocket", u"Last Srike:", None))
        self.lastStrike.setText(QCoreApplication.translate("websocket", u"\u221e", None))
        self.lastStrike.setProperty("measurement", QCoreApplication.translate("websocket", u"wind", None))
        self.strikeDistanceLabel.setText(QCoreApplication.translate("websocket", u"Distance:", None))
        self.strikeDistance.setText(QCoreApplication.translate("websocket", u"\u221e", None))
        self.strikeDistance.setProperty("measurement", QCoreApplication.translate("websocket", u"windDirection", None))
        self.strikeEnergyLabel.setText(QCoreApplication.translate("websocket", u"Energy:", None))
        self.strikeEnergy.setText(QCoreApplication.translate("websocket", u"0", None))
        self.strikeEnergy.setProperty("measurement", QCoreApplication.translate("websocket", u"windDirection", None))
        self.strikeTotalLabel.setText(QCoreApplication.translate("websocket", u"Total:", None))
        self.strikeTotal.setText(QCoreApplication.translate("websocket", u"0", None))
        self.strikeTotal.setProperty("measurement", QCoreApplication.translate("websocket", u"windDirection", None))
    # retranslateUi

