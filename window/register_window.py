# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'register_window.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(382, 568)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(382, 568))
        MainWindow.setMaximumSize(QSize(382, 568))
        MainWindow.setStyleSheet(u"background-color: rgb(252, 252, 252);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.lbl_username = QLabel(self.centralwidget)
        self.lbl_username.setObjectName(u"lbl_username")
        self.lbl_username.setGeometry(QRect(40, 140, 81, 21))
        self.lbl_username.setStyleSheet(u"font-size: 12px;\n"
"color: #444;")
        self.lbl_password = QLabel(self.centralwidget)
        self.lbl_password.setObjectName(u"lbl_password")
        self.lbl_password.setGeometry(QRect(40, 220, 81, 21))
        self.lbl_password.setStyleSheet(u"font-size: 12px;\n"
"color: #444;")
        self.btn_register = QPushButton(self.centralwidget)
        self.btn_register.setObjectName(u"btn_register")
        self.btn_register.setGeometry(QRect(10, 410, 361, 41))
        self.btn_register.setStyleSheet(u"QPushButton {\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5,\n"
"                                    stop:0 #00d4ff, stop:1 #ff00d4);\n"
"border-radius: 20px;\n"
"color: white;\n"
"font-size: 16px;\n"
"font-weight: bold;\n"
"padding: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5,\n"
"                                            stop:0 #00c3e0, stop:1 #e000c3);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5,\n"
"                                      stop:0 #009bb8, stop:1 #b0009b);\n"
"}")
        self.le_password = QLineEdit(self.centralwidget)
        self.le_password.setObjectName(u"le_password")
        self.le_password.setGeometry(QRect(40, 240, 311, 41))
        self.le_password.setStyleSheet(u"border: none;\n"
"border-bottom: 1px solid #444;\n"
"font-size: 14px;\n"
"color: #444;\n"
"padding: 5px;\n"
"\n"
"")
        self.le_password.setEchoMode(QLineEdit.EchoMode.Password)
        self.le_username = QLineEdit(self.centralwidget)
        self.le_username.setObjectName(u"le_username")
        self.le_username.setGeometry(QRect(40, 160, 311, 41))
        self.le_username.setStyleSheet(u"border: none;\n"
"border-bottom: 1px solid #444;\n"
"font-size: 14px;\n"
"color: #444;\n"
"padding: 5px;\n"
"\n"
"")
        self.le_confirm_password = QLineEdit(self.centralwidget)
        self.le_confirm_password.setObjectName(u"le_confirm_password")
        self.le_confirm_password.setGeometry(QRect(40, 320, 311, 41))
        self.le_confirm_password.setStyleSheet(u"border: none;\n"
"border-bottom: 1px solid #444;\n"
"font-size: 14px;\n"
"color: #444;\n"
"padding: 5px;\n"
"\n"
"")
        self.le_confirm_password.setEchoMode(QLineEdit.EchoMode.Password)
        self.lbl_confirm_password = QLabel(self.centralwidget)
        self.lbl_confirm_password.setObjectName(u"lbl_confirm_password")
        self.lbl_confirm_password.setGeometry(QRect(40, 300, 111, 21))
        self.lbl_confirm_password.setStyleSheet(u"font-size: 12px;\n"
"color: #444;")
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 40, 360, 69))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_2 = QSpacerItem(108, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.lbl_register = QLabel(self.layoutWidget)
        self.lbl_register.setObjectName(u"lbl_register")
        self.lbl_register.setStyleSheet(u"color: #1A1B1F;\n"
"font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;\n"
"font-size: 32px;\n"
"font-weight: 600;\n"
"letter-spacing: -0.5px;\n"
"margin-bottom: 24px;\n"
"text-align: left;\n"
"padding: 0;\n"
"line-height: 1.3;")

        self.horizontalLayout.addWidget(self.lbl_register)

        self.horizontalSpacer = QSpacerItem(108, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        MainWindow.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.le_username, self.le_password)
        QWidget.setTabOrder(self.le_password, self.le_confirm_password)
        QWidget.setTabOrder(self.le_confirm_password, self.btn_register)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"ProductManager", None))
        self.lbl_username.setText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.lbl_password.setText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.btn_register.setText(QCoreApplication.translate("MainWindow", u"REGISTER NOW", None))
        self.le_password.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Type your password", None))
        self.le_username.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Type your username", None))
        self.le_confirm_password.setText("")
        self.le_confirm_password.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Repeat your password", None))
        self.lbl_confirm_password.setText(QCoreApplication.translate("MainWindow", u"Confirm password", None))
        self.lbl_register.setText(QCoreApplication.translate("MainWindow", u"Register", None))
    # retranslateUi

