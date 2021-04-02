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


class Ui_websocket(object):
    def setupUi(self, websocket):
        if not websocket.objectName():
            websocket.setObjectName(u"websocket")
        websocket.resize(1294, 555)
        self.gridLayout = QGridLayout(websocket)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(10)
        self.gridLayout.setVerticalSpacing(0)
        self.gridLayout.setContentsMargins(-1, -1, 12, 0)
        self.skyGroup = QGroupBox(websocket)
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
        self.strikeDistance = QLabel(self.skyGroup)
        self.strikeDistance.setObjectName(u"strikeDistance")
        font1 = QFont()
        font1.setPointSize(24)
        self.strikeDistance.setFont(font1)

        self.gridLayout_2.addWidget(self.strikeDistance, 2, 1, 1, 1)

        self.precipRateLabel = QLabel(self.skyGroup)
        self.precipRateLabel.setObjectName(u"precipRateLabel")
        self.precipRateLabel.setFont(font1)

        self.gridLayout_2.addWidget(self.precipRateLabel, 0, 0, 1, 1)

        self.precipRate = QLabel(self.skyGroup)
        self.precipRate.setObjectName(u"precipRate")
        self.precipRate.setFont(font1)

        self.gridLayout_2.addWidget(self.precipRate, 0, 1, 1, 1)

        self.strikeDistanceLabel = QLabel(self.skyGroup)
        self.strikeDistanceLabel.setObjectName(u"strikeDistanceLabel")
        self.strikeDistanceLabel.setFont(font1)

        self.gridLayout_2.addWidget(self.strikeDistanceLabel, 2, 0, 1, 1)

        self.strikes = QLabel(self.skyGroup)
        self.strikes.setObjectName(u"strikes")
        self.strikes.setFont(font1)

        self.gridLayout_2.addWidget(self.strikes, 1, 1, 1, 1)

        self.strikesLabel = QLabel(self.skyGroup)
        self.strikesLabel.setObjectName(u"strikesLabel")
        self.strikesLabel.setFont(font1)

        self.gridLayout_2.addWidget(self.strikesLabel, 1, 0, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_4, 3, 0, 1, 1)


        self.gridLayout.addWidget(self.skyGroup, 0, 3, 1, 1)

        self.solarGroup = QGroupBox(websocket)
        self.solarGroup.setObjectName(u"solarGroup")
        self.solarGroup.setMinimumSize(QSize(320, 0))
        self.solarGroup.setMaximumSize(QSize(320, 16777215))
        self.solarGroup.setFont(font)
        self.solarGridLayout = QGridLayout(self.solarGroup)
        self.solarGridLayout.setObjectName(u"solarGridLayout")
        self.uv = QLabel(self.solarGroup)
        self.uv.setObjectName(u"uv")
        self.uv.setFont(font1)

        self.solarGridLayout.addWidget(self.uv, 2, 1, 1, 1)

        self.irradiance = QLabel(self.solarGroup)
        self.irradiance.setObjectName(u"irradiance")
        self.irradiance.setFont(font1)

        self.solarGridLayout.addWidget(self.irradiance, 1, 1, 1, 1)

        self.irradianceLabel = QLabel(self.solarGroup)
        self.irradianceLabel.setObjectName(u"irradianceLabel")
        self.irradianceLabel.setFont(font1)

        self.solarGridLayout.addWidget(self.irradianceLabel, 1, 0, 1, 1)

        self.illuminance = QLabel(self.solarGroup)
        self.illuminance.setObjectName(u"illuminance")
        self.illuminance.setFont(font1)

        self.solarGridLayout.addWidget(self.illuminance, 0, 1, 1, 1)

        self.illuminanceLabel = QLabel(self.solarGroup)
        self.illuminanceLabel.setObjectName(u"illuminanceLabel")
        self.illuminanceLabel.setFont(font1)

        self.solarGridLayout.addWidget(self.illuminanceLabel, 0, 0, 1, 1)

        self.uvLabel = QLabel(self.solarGroup)
        self.uvLabel.setObjectName(u"uvLabel")
        self.uvLabel.setFont(font1)

        self.solarGridLayout.addWidget(self.uvLabel, 2, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.solarGridLayout.addItem(self.verticalSpacer_2, 3, 0, 1, 1)


        self.gridLayout.addWidget(self.solarGroup, 0, 2, 1, 1)

        self.windGroup = QGroupBox(websocket)
        self.windGroup.setObjectName(u"windGroup")
        self.windGroup.setMinimumSize(QSize(320, 0))
        self.windGroup.setMaximumSize(QSize(320, 16777215))
        self.windGroup.setFont(font)
        self.gridLayout_3 = QGridLayout(self.windGroup)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.groupBox = QGroupBox(self.windGroup)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy1)
        font2 = QFont()
        font2.setPointSize(26)
        font2.setBold(True)
        self.groupBox.setFont(font2)
        self.groupBox.setFlat(True)
        self.groupBox.setCheckable(False)
        self.formLayout = QFormLayout(self.groupBox)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setFieldGrowthPolicy(QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setLabelAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.formLayout.setHorizontalSpacing(-1)
        self.formLayout.setVerticalSpacing(-1)
        self.formLayout.setContentsMargins(0, -1, 0, -1)
        self.windLabel = QLabel(self.groupBox)
        self.windLabel.setObjectName(u"windLabel")
        font3 = QFont()
        font3.setPointSize(24)
        font3.setBold(False)
        self.windLabel.setFont(font3)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.windLabel)

        self.wind = QLabel(self.groupBox)
        self.wind.setObjectName(u"wind")
        self.wind.setFont(font3)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.wind)

        self.windDirectionLabel = QLabel(self.groupBox)
        self.windDirectionLabel.setObjectName(u"windDirectionLabel")
        self.windDirectionLabel.setFont(font3)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.windDirectionLabel)

        self.windDirection = QLabel(self.groupBox)
        self.windDirection.setObjectName(u"windDirection")
        self.windDirection.setFont(font3)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.windDirection)


        self.gridLayout_3.addWidget(self.groupBox, 0, 0, 1, 1)

        self.groupBox_2 = QGroupBox(self.windGroup)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setFont(font2)
        self.groupBox_2.setFlat(True)
        self.formLayout_2 = QFormLayout(self.groupBox_2)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setFieldGrowthPolicy(QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_2.setLabelAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.formLayout_2.setContentsMargins(0, -1, -1, -1)
        self.lullLabel = QLabel(self.groupBox_2)
        self.lullLabel.setObjectName(u"lullLabel")
        self.lullLabel.setFont(font3)

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.lullLabel)

        self.lull = QLabel(self.groupBox_2)
        self.lull.setObjectName(u"lull")
        self.lull.setFont(font3)

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.lull)

        self.gustLabel = QLabel(self.groupBox_2)
        self.gustLabel.setObjectName(u"gustLabel")
        self.gustLabel.setFont(font3)

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.gustLabel)

        self.gust = QLabel(self.groupBox_2)
        self.gust.setObjectName(u"gust")
        self.gust.setFont(font3)

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.gust)

        self.windAverageLabel = QLabel(self.groupBox_2)
        self.windAverageLabel.setObjectName(u"windAverageLabel")
        self.windAverageLabel.setFont(font3)

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.windAverageLabel)

        self.windAverage = QLabel(self.groupBox_2)
        self.windAverage.setObjectName(u"windAverage")
        self.windAverage.setFont(font3)

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.windAverage)

        self.windDirectionAverageLabel = QLabel(self.groupBox_2)
        self.windDirectionAverageLabel.setObjectName(u"windDirectionAverageLabel")
        self.windDirectionAverageLabel.setFont(font3)

        self.formLayout_2.setWidget(3, QFormLayout.LabelRole, self.windDirectionAverageLabel)

        self.windDirectionAverage = QLabel(self.groupBox_2)
        self.windDirectionAverage.setObjectName(u"windDirectionAverage")
        self.windDirectionAverage.setFont(font3)

        self.formLayout_2.setWidget(3, QFormLayout.FieldRole, self.windDirectionAverage)


        self.gridLayout_3.addWidget(self.groupBox_2, 1, 0, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_3, 2, 0, 1, 1)


        self.gridLayout.addWidget(self.windGroup, 0, 1, 1, 1)

        self.airGroup = QGroupBox(websocket)
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
        self.temperatureLabel.setFont(font3)

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.temperatureLabel)

        self.temperature = QLabel(self.airGroup)
        self.temperature.setObjectName(u"temperature")
        self.temperature.setFont(font3)

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.temperature)

        self.humidityLabel = QLabel(self.airGroup)
        self.humidityLabel.setObjectName(u"humidityLabel")
        self.humidityLabel.setFont(font3)

        self.formLayout_3.setWidget(1, QFormLayout.LabelRole, self.humidityLabel)

        self.humidity = QLabel(self.airGroup)
        self.humidity.setObjectName(u"humidity")
        self.humidity.setFont(font3)

        self.formLayout_3.setWidget(1, QFormLayout.FieldRole, self.humidity)

        self.feelsLikeLabel = QLabel(self.airGroup)
        self.feelsLikeLabel.setObjectName(u"feelsLikeLabel")
        self.feelsLikeLabel.setFont(font3)

        self.formLayout_3.setWidget(2, QFormLayout.LabelRole, self.feelsLikeLabel)

        self.feelsLike = QLabel(self.airGroup)
        self.feelsLike.setObjectName(u"feelsLike")
        self.feelsLike.setFont(font3)

        self.formLayout_3.setWidget(2, QFormLayout.FieldRole, self.feelsLike)

        self.dewpointLabel = QLabel(self.airGroup)
        self.dewpointLabel.setObjectName(u"dewpointLabel")
        self.dewpointLabel.setFont(font3)

        self.formLayout_3.setWidget(3, QFormLayout.LabelRole, self.dewpointLabel)

        self.dewpoint = QLabel(self.airGroup)
        self.dewpoint.setObjectName(u"dewpoint")
        self.dewpoint.setFont(font3)

        self.formLayout_3.setWidget(3, QFormLayout.FieldRole, self.dewpoint)

        self.airDensityLabel = QLabel(self.airGroup)
        self.airDensityLabel.setObjectName(u"airDensityLabel")
        self.airDensityLabel.setFont(font3)

        self.formLayout_3.setWidget(4, QFormLayout.LabelRole, self.airDensityLabel)

        self.airDensity = QLabel(self.airGroup)
        self.airDensity.setObjectName(u"airDensity")
        self.airDensity.setFont(font3)

        self.formLayout_3.setWidget(4, QFormLayout.FieldRole, self.airDensity)

        self.pressureLabel = QLabel(self.airGroup)
        self.pressureLabel.setObjectName(u"pressureLabel")
        self.pressureLabel.setFont(font3)

        self.formLayout_3.setWidget(5, QFormLayout.LabelRole, self.pressureLabel)

        self.pressure = QLabel(self.airGroup)
        self.pressure.setObjectName(u"pressure")
        self.pressure.setFont(font3)

        self.formLayout_3.setWidget(5, QFormLayout.FieldRole, self.pressure)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.formLayout_3.setItem(6, QFormLayout.LabelRole, self.verticalSpacer)


        self.gridLayout.addWidget(self.airGroup, 0, 0, 1, 1)

#if QT_CONFIG(shortcut)
        self.precipRateLabel.setBuddy(self.precipRate)
        self.strikeDistanceLabel.setBuddy(self.strikeDistance)
        self.strikesLabel.setBuddy(self.strikes)
#endif // QT_CONFIG(shortcut)

        self.retranslateUi(websocket)

        QMetaObject.connectSlotsByName(websocket)
    # setupUi

    def retranslateUi(self, websocket):
        websocket.setWindowTitle(QCoreApplication.translate("websocket", u"Form", None))
        self.skyGroup.setTitle(QCoreApplication.translate("websocket", u"Sky", None))
        self.strikeDistance.setText("")
        self.strikeDistance.setProperty("measurement", QCoreApplication.translate("websocket", u"lightningDistance", None))
        self.precipRateLabel.setText(QCoreApplication.translate("websocket", u"Precipitation Rate", None))
        self.precipRate.setText("")
        self.precipRate.setProperty("measurement", QCoreApplication.translate("websocket", u"precipitationHourlyRaw", None))
        self.strikeDistanceLabel.setText(QCoreApplication.translate("websocket", u"Strike Distance:", None))
        self.strikes.setText("")
        self.strikes.setProperty("measurement", QCoreApplication.translate("websocket", u"lightning", None))
        self.strikesLabel.setText(QCoreApplication.translate("websocket", u"Strikes:", None))
        self.solarGroup.setTitle(QCoreApplication.translate("websocket", u"Solar", None))
        self.uv.setText("")
        self.uv.setProperty("measurement", "")
        self.irradiance.setText("")
        self.irradiance.setProperty("measurement", "")
        self.irradianceLabel.setText(QCoreApplication.translate("websocket", u"Solar Radiation:", None))
        self.illuminance.setText("")
        self.illuminance.setProperty("measurement", "")
        self.illuminanceLabel.setText(QCoreApplication.translate("websocket", u"Illuminance:", None))
        self.uvLabel.setText(QCoreApplication.translate("websocket", u"UV:", None))
        self.windGroup.setTitle(QCoreApplication.translate("websocket", u"Wind", None))
        self.groupBox.setTitle(QCoreApplication.translate("websocket", u"Now", None))
        self.windLabel.setText(QCoreApplication.translate("websocket", u"Speed:", None))
        self.wind.setText("")
        self.wind.setProperty("measurement", QCoreApplication.translate("websocket", u"wind", None))
        self.windDirectionLabel.setText(QCoreApplication.translate("websocket", u"Direction:", None))
        self.windDirection.setText("")
        self.windDirection.setProperty("measurement", QCoreApplication.translate("websocket", u"windDirection", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("websocket", u"Averages", None))
        self.lullLabel.setText(QCoreApplication.translate("websocket", u"Lull:", None))
        self.lull.setText("")
        self.lull.setProperty("measurement", QCoreApplication.translate("websocket", u"lullSpeed", None))
        self.gustLabel.setText(QCoreApplication.translate("websocket", u"Gust:", None))
        self.gust.setText("")
        self.gust.setProperty("measurement", QCoreApplication.translate("websocket", u"gustSpeed", None))
        self.windAverageLabel.setText(QCoreApplication.translate("websocket", u"Speed", None))
        self.windAverage.setText("")
        self.windAverage.setProperty("measurement", QCoreApplication.translate("websocket", u"windAverage", None))
        self.windDirectionAverageLabel.setText(QCoreApplication.translate("websocket", u"Direction:", None))
        self.windDirectionAverage.setText("")
        self.windDirectionAverage.setProperty("measurement", QCoreApplication.translate("websocket", u"windDirection", None))
        self.airGroup.setTitle(QCoreApplication.translate("websocket", u"Air", None))
        self.temperatureLabel.setText(QCoreApplication.translate("websocket", u"Temperature:", None))
        self.temperature.setText(QCoreApplication.translate("websocket", u"0", None))
        self.temperature.setProperty("measurement", QCoreApplication.translate("websocket", u"temperature", None))
        self.humidityLabel.setText(QCoreApplication.translate("websocket", u"Humidity:", None))
        self.humidity.setText(QCoreApplication.translate("websocket", u"0", None))
        self.humidity.setProperty("measurement", QCoreApplication.translate("websocket", u"humidity", None))
        self.feelsLikeLabel.setText(QCoreApplication.translate("websocket", u"Feels Like:", None))
        self.feelsLike.setText(QCoreApplication.translate("websocket", u"0", None))
        self.feelsLike.setProperty("measurement", QCoreApplication.translate("websocket", u"temperature", None))
        self.dewpointLabel.setText(QCoreApplication.translate("websocket", u"Dew Point:", None))
        self.dewpoint.setText(QCoreApplication.translate("websocket", u"0", None))
        self.dewpoint.setProperty("measurement", QCoreApplication.translate("websocket", u"temperature", None))
        self.airDensityLabel.setText(QCoreApplication.translate("websocket", u"Air Density:", None))
        self.airDensity.setText(QCoreApplication.translate("websocket", u"0", None))
        self.airDensity.setProperty("measurement", QCoreApplication.translate("websocket", u"pressure", None))
        self.pressureLabel.setText(QCoreApplication.translate("websocket", u"Pressure:", None))
        self.pressure.setText(QCoreApplication.translate("websocket", u"0", None))
        self.pressure.setProperty("measurement", QCoreApplication.translate("websocket", u"pressure", None))
    # retranslateUi

