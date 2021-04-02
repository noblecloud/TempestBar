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

from ui.socketsUI import UDPTab
from ui.socketsUI import WSTab


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(925, 427)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.tabs = QTabWidget(self.centralwidget)
        self.tabs.setObjectName(u"tabs")
        self.tabs.setTabShape(QTabWidget.Rounded)
        self.tabs.setUsesScrollButtons(False)
        self.udp = QWidget()
        self.udp.setObjectName(u"udp")
        self.verticalLayout = QVBoxLayout(self.udp)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.udpFrame = UDPTab(self.udp)
        self.udpFrame.setObjectName(u"udpFrame")
        self.udpFrame.setFrameShape(QFrame.NoFrame)
        self.udpFrame.setFrameShadow(QFrame.Plain)

        self.verticalLayout.addWidget(self.udpFrame)

        self.tabs.addTab(self.udp, "")
        self.webSocket = QWidget()
        self.webSocket.setObjectName(u"webSocket")
        self.verticalLayout_2 = QVBoxLayout(self.webSocket)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.webFrame = WSTab(self.webSocket)
        self.webFrame.setObjectName(u"webFrame")
        self.webFrame.setFrameShape(QFrame.NoFrame)
        self.webFrame.setFrameShadow(QFrame.Plain)
        self.webFrame.setLineWidth(0)

        self.verticalLayout_2.addWidget(self.webFrame)

        self.tabs.addTab(self.webSocket, "")
        self.status = QWidget()
        self.status.setObjectName(u"status")
        self.gridLayout_3 = QGridLayout(self.status)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.hubGroup = QGroupBox(self.status)
        self.hubGroup.setObjectName(u"hubGroup")
        self.hubGroup.setMaximumSize(QSize(300, 16777215))
        font = QFont()
        font.setPointSize(34)
        self.hubGroup.setFont(font)
        self.hubGroupLayout = QGridLayout(self.hubGroup)
        self.hubGroupLayout.setObjectName(u"hubGroupLayout")
        self.hubSerialLabel = QLabel(self.hubGroup)
        self.hubSerialLabel.setObjectName(u"hubSerialLabel")
        font1 = QFont()
        font1.setPointSize(24)
        self.hubSerialLabel.setFont(font1)

        self.hubGroupLayout.addWidget(self.hubSerialLabel, 0, 0, 1, 1)

        self.hubUptimeLabel = QLabel(self.hubGroup)
        self.hubUptimeLabel.setObjectName(u"hubUptimeLabel")
        self.hubUptimeLabel.setFont(font1)

        self.hubGroupLayout.addWidget(self.hubUptimeLabel, 2, 0, 1, 1)

        self.hubUptime = QLabel(self.hubGroup)
        self.hubUptime.setObjectName(u"hubUptime")
        self.hubUptime.setFont(font1)

        self.hubGroupLayout.addWidget(self.hubUptime, 2, 1, 1, 1)

        self.hubFirmware = QLabel(self.hubGroup)
        self.hubFirmware.setObjectName(u"hubFirmware")
        self.hubFirmware.setFont(font1)

        self.hubGroupLayout.addWidget(self.hubFirmware, 1, 1, 1, 1)

        self.hubSerial = QLabel(self.hubGroup)
        self.hubSerial.setObjectName(u"hubSerial")
        self.hubSerial.setFont(font1)

        self.hubGroupLayout.addWidget(self.hubSerial, 0, 1, 1, 1)

        self.hubFirmwareLabel = QLabel(self.hubGroup)
        self.hubFirmwareLabel.setObjectName(u"hubFirmwareLabel")
        self.hubFirmwareLabel.setFont(font1)

        self.hubGroupLayout.addWidget(self.hubFirmwareLabel, 1, 0, 1, 1)


        self.gridLayout_3.addWidget(self.hubGroup, 0, 0, 1, 1)

        self.deviceGroup = QGroupBox(self.status)
        self.deviceGroup.setObjectName(u"deviceGroup")
        self.deviceGroup.setMaximumSize(QSize(300, 16777215))
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


        self.gridLayout_3.addWidget(self.deviceGroup, 0, 1, 1, 1)

        self.tabs.addTab(self.status, "")

        self.verticalLayout_3.addWidget(self.tabs)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Plain)
        self.frame.setLineWidth(0)
        self.horizontalLayout_3 = QHBoxLayout(self.frame)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.connectionToggle_2 = QPushButton(self.frame)
        self.connectionToggle_2.setObjectName(u"connectionToggle_2")
        self.connectionToggle_2.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_3.addWidget(self.connectionToggle_2)

        self.comboBox_2 = QComboBox(self.frame)
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_3.addWidget(self.comboBox_2)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)


        self.verticalLayout_3.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 925, 24))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabs.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.tabs.setTabText(self.tabs.indexOf(self.udp), QCoreApplication.translate("MainWindow", u"UDP", None))
        self.tabs.setTabText(self.tabs.indexOf(self.webSocket), QCoreApplication.translate("MainWindow", u"WebSocket", None))
        self.hubGroup.setTitle(QCoreApplication.translate("MainWindow", u"Hub Status", None))
        self.hubSerialLabel.setText(QCoreApplication.translate("MainWindow", u"Serial:", None))
        self.hubUptimeLabel.setText(QCoreApplication.translate("MainWindow", u"Uptime:", None))
        self.hubUptime.setText("")
        self.hubUptime.setProperty("measurement", "")
        self.hubFirmware.setText("")
        self.hubFirmware.setProperty("measurement", "")
        self.hubSerial.setText("")
        self.hubSerial.setProperty("measurement", "")
        self.hubFirmwareLabel.setText(QCoreApplication.translate("MainWindow", u"Firmware:", None))
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
        self.tabs.setTabText(self.tabs.indexOf(self.status), QCoreApplication.translate("MainWindow", u"Status", None))
        self.connectionToggle_2.setText(QCoreApplication.translate("MainWindow", u"Connect", None))
    # retranslateUi

