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


class Ui_status(object):
    def setupUi(self, status):
        if not status.objectName():
            status.setObjectName(u"status")
        status.resize(1312, 431)
        status.setMinimumSize(QSize(1312, 431))
        self.horizontalLayout = QHBoxLayout(status)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.hubGroup = QGroupBox(status)
        self.hubGroup.setObjectName(u"hubGroup")
        font = QFont()
        font.setPointSize(34)
        self.hubGroup.setFont(font)
        self.formLayout = QFormLayout(self.hubGroup)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setFieldGrowthPolicy(QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setLabelAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.formLayout.setContentsMargins(-1, 0, -1, 0)
        self.hubSerialLabel = QLabel(self.hubGroup)
        self.hubSerialLabel.setObjectName(u"hubSerialLabel")
        font1 = QFont()
        font1.setPointSize(24)
        self.hubSerialLabel.setFont(font1)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.hubSerialLabel)

        self.hubSerial = QLabel(self.hubGroup)
        self.hubSerial.setObjectName(u"hubSerial")
        self.hubSerial.setFont(font1)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.hubSerial)

        self.hubFirmwareLabel = QLabel(self.hubGroup)
        self.hubFirmwareLabel.setObjectName(u"hubFirmwareLabel")
        self.hubFirmwareLabel.setFont(font1)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.hubFirmwareLabel)

        self.hubFirmware = QLabel(self.hubGroup)
        self.hubFirmware.setObjectName(u"hubFirmware")
        self.hubFirmware.setFont(font1)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.hubFirmware)

        self.hubUptimeLabel = QLabel(self.hubGroup)
        self.hubUptimeLabel.setObjectName(u"hubUptimeLabel")
        self.hubUptimeLabel.setFont(font1)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.hubUptimeLabel)

        self.hubUptime = QLabel(self.hubGroup)
        self.hubUptime.setObjectName(u"hubUptime")
        self.hubUptime.setFont(font1)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.hubUptime)


        self.horizontalLayout.addWidget(self.hubGroup)

        self.deviceGroup = QGroupBox(status)
        self.deviceGroup.setObjectName(u"deviceGroup")
        self.deviceGroup.setFont(font)
        self.formLayout_2 = QFormLayout(self.deviceGroup)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setFieldGrowthPolicy(QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_2.setLabelAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.formLayout_2.setContentsMargins(12, 0, 12, 0)
        self.deviceSerialLabel = QLabel(self.deviceGroup)
        self.deviceSerialLabel.setObjectName(u"deviceSerialLabel")
        self.deviceSerialLabel.setFont(font1)

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.deviceSerialLabel)

        self.deviceSerial = QLabel(self.deviceGroup)
        self.deviceSerial.setObjectName(u"deviceSerial")
        self.deviceSerial.setFont(font1)

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.deviceSerial)

        self.deviceFirmwareLabel = QLabel(self.deviceGroup)
        self.deviceFirmwareLabel.setObjectName(u"deviceFirmwareLabel")
        self.deviceFirmwareLabel.setFont(font1)

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.deviceFirmwareLabel)

        self.deviceFirmware = QLabel(self.deviceGroup)
        self.deviceFirmware.setObjectName(u"deviceFirmware")
        self.deviceFirmware.setFont(font1)

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.deviceFirmware)

        self.deviceUptimeLabel = QLabel(self.deviceGroup)
        self.deviceUptimeLabel.setObjectName(u"deviceUptimeLabel")
        self.deviceUptimeLabel.setFont(font1)

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.deviceUptimeLabel)

        self.deviceUptime = QLabel(self.deviceGroup)
        self.deviceUptime.setObjectName(u"deviceUptime")
        self.deviceUptime.setFont(font1)

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.deviceUptime)

        self.deviceSensorsLabel = QLabel(self.deviceGroup)
        self.deviceSensorsLabel.setObjectName(u"deviceSensorsLabel")
        self.deviceSensorsLabel.setFont(font1)

        self.formLayout_2.setWidget(3, QFormLayout.LabelRole, self.deviceSensorsLabel)

        self.deviceSensors = QLabel(self.deviceGroup)
        self.deviceSensors.setObjectName(u"deviceSensors")
        self.deviceSensors.setFont(font1)

        self.formLayout_2.setWidget(3, QFormLayout.FieldRole, self.deviceSensors)

        self.deviceBatteryLabel = QLabel(self.deviceGroup)
        self.deviceBatteryLabel.setObjectName(u"deviceBatteryLabel")
        self.deviceBatteryLabel.setFont(font1)

        self.formLayout_2.setWidget(4, QFormLayout.LabelRole, self.deviceBatteryLabel)

        self.deviceBattery = QLabel(self.deviceGroup)
        self.deviceBattery.setObjectName(u"deviceBattery")
        self.deviceBattery.setFont(font1)

        self.formLayout_2.setWidget(4, QFormLayout.FieldRole, self.deviceBattery)


        self.horizontalLayout.addWidget(self.deviceGroup)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.retranslateUi(status)

        QMetaObject.connectSlotsByName(status)
    # setupUi

    def retranslateUi(self, status):
        status.setWindowTitle(QCoreApplication.translate("status", u"Form", None))
        self.hubGroup.setTitle(QCoreApplication.translate("status", u"Hub Status", None))
        self.hubSerialLabel.setText(QCoreApplication.translate("status", u"Serial:", None))
        self.hubSerial.setText("")
        self.hubSerial.setProperty("measurement", "")
        self.hubFirmwareLabel.setText(QCoreApplication.translate("status", u"Firmware:", None))
        self.hubFirmware.setText("")
        self.hubFirmware.setProperty("measurement", "")
        self.hubUptimeLabel.setText(QCoreApplication.translate("status", u"Uptime:", None))
        self.hubUptime.setText("")
        self.hubUptime.setProperty("measurement", "")
        self.deviceGroup.setTitle(QCoreApplication.translate("status", u"Device Status", None))
        self.deviceSerialLabel.setText(QCoreApplication.translate("status", u"Serial:", None))
        self.deviceSerial.setText("")
        self.deviceSerial.setProperty("measurement", "")
        self.deviceFirmwareLabel.setText(QCoreApplication.translate("status", u"Firmware:", None))
        self.deviceFirmware.setText("")
        self.deviceFirmware.setProperty("measurement", "")
        self.deviceUptimeLabel.setText(QCoreApplication.translate("status", u"Uptime:", None))
        self.deviceUptime.setText("")
        self.deviceUptime.setProperty("measurement", "")
        self.deviceSensorsLabel.setText(QCoreApplication.translate("status", u"Sensors:", None))
        self.deviceSensors.setText("")
        self.deviceSensors.setProperty("measurement", "")
        self.deviceBatteryLabel.setText(QCoreApplication.translate("status", u"Battery:", None))
        self.deviceBattery.setText("")
        self.deviceBattery.setProperty("measurement", "")
    # retranslateUi

