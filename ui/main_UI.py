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

from ui.socketsUI import Info


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowModality(Qt.WindowModal)
        MainWindow.resize(504, 350)
        MainWindow.setMinimumSize(QSize(0, 350))
        MainWindow.setMaximumSize(QSize(16777215, 350))
        MainWindow.setMouseTracking(True)
        MainWindow.setWindowTitle(u"TempestBar")
        MainWindow.setDocumentMode(True)
        self.info = Info(MainWindow)
        self.info.setObjectName(u"info")
        MainWindow.setCentralWidget(self.info)

        self.retranslateUi(MainWindow)
        self.info.connectionSignal.connect(self.info.hide)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        pass
    # retranslateUi

