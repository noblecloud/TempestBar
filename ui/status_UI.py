# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'status.ui'
##
## Created by: Qt User Interface Compiler version 6.0.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from ui.flowLayout import FlowLayout as QHBoxLayout

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.resize(655, 353)
        self.horizontalLayout = QHBoxLayout(Dialog)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.hubGroup = QGroupBox(Dialog)
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


        self.horizontalLayout.addWidget(self.hubGroup)

        self.deviceGroup = QGroupBox(Dialog)
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


        self.horizontalLayout.addWidget(self.deviceGroup)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.hubGroup.setTitle(QCoreApplication.translate("Dialog", u"Hub Status", None))
        self.hubFirmwareLabel.setText(QCoreApplication.translate("Dialog", u"Firmware:", None))
        self.hubUptime.setText("")
        self.hubUptime.setProperty("measurement", "")
        self.hubSerialLabel.setText(QCoreApplication.translate("Dialog", u"Serial:", None))
        self.hubSerial.setText("")
        self.hubSerial.setProperty("measurement", "")
        self.hubFirmware.setText("")
        self.hubFirmware.setProperty("measurement", "")
        self.hubUptimeLabel.setText(QCoreApplication.translate("Dialog", u"Uptime:", None))
        self.deviceGroup.setTitle(QCoreApplication.translate("Dialog", u"Device Status", None))
        self.deviceSerial.setText("")
        self.deviceSerial.setProperty("measurement", "")
        self.deviceFirmware.setText("")
        self.deviceFirmware.setProperty("measurement", "")
        self.deviceFirmwareLabel.setText(QCoreApplication.translate("Dialog", u"Firmware:", None))
        self.deviceSerialLabel.setText(QCoreApplication.translate("Dialog", u"Serial:", None))
        self.deviceSensorsLabel.setText(QCoreApplication.translate("Dialog", u"Sensors:", None))
        self.deviceSensors.setText("")
        self.deviceSensors.setProperty("measurement", "")
        self.deviceUptimeLabel.setText(QCoreApplication.translate("Dialog", u"Uptime:", None))
        self.deviceUptime.setText("")
        self.deviceUptime.setProperty("measurement", "")
        self.deviceBatteryLabel.setText(QCoreApplication.translate("Dialog", u"Battery:", None))
        self.deviceBattery.setText("")
        self.deviceBattery.setProperty("measurement", "")
    # retranslateUi

