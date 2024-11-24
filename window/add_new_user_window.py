# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_new_user_window.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QWidget)

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
        self.lbl_username.setGeometry(QRect(40, 110, 81, 21))
        self.lbl_username.setStyleSheet(u"font-size: 12px;\n"
"color: #444;")
        self.lbl_password = QLabel(self.centralwidget)
        self.lbl_password.setObjectName(u"lbl_password")
        self.lbl_password.setGeometry(QRect(40, 190, 81, 21))
        self.lbl_password.setStyleSheet(u"font-size: 12px;\n"
"color: #444;")
        self.btn_register_user = QPushButton(self.centralwidget)
        self.btn_register_user.setObjectName(u"btn_register_user")
        self.btn_register_user.setGeometry(QRect(10, 490, 361, 41))
        self.btn_register_user.setStyleSheet(u"QPushButton {\n"
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
        self.le_password.setGeometry(QRect(40, 210, 311, 41))
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
        self.le_username.setGeometry(QRect(40, 130, 311, 41))
        self.le_username.setStyleSheet(u"border: none;\n"
"border-bottom: 1px solid #444;\n"
"font-size: 14px;\n"
"color: #444;\n"
"padding: 5px;\n"
"\n"
"")
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(-20, 40, 422, 69))
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

        self.lbl_username_7 = QLabel(self.centralwidget)
        self.lbl_username_7.setObjectName(u"lbl_username_7")
        self.lbl_username_7.setGeometry(QRect(40, 270, 101, 21))
        self.lbl_username_7.setStyleSheet(u"font-size: 12px;\n"
"color: #444;")
        self.cb_user_root = QComboBox(self.centralwidget)
        self.cb_user_root.addItem("")
        self.cb_user_root.addItem("")
        self.cb_user_root.addItem("")
        self.cb_user_root.setObjectName(u"cb_user_root")
        self.cb_user_root.setGeometry(QRect(40, 290, 311, 41))
        self.cb_user_root.setStyleSheet(u"QComboBox {\n"
"background-color: white;\n"
"border: 1px solid rgba(152, 159, 181, 30);\n"
"border-radius: 8px;\n"
"font-size: 14px;\n"
"color: black;\n"
"padding-left: 10px;\n"
"\n"
"border-bottom: 1px solid #444;\n"
"color: #444;\n"
"padding: 5px;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    border: none;\n"
"    width: 20px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    background-color: white;\n"
"    selection-background-color: #0366d6;\n"
"    selection-color: white;\n"
"    color: #24292e;\n"
"}")
        MainWindow.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.le_username, self.le_password)
        QWidget.setTabOrder(self.le_password, self.btn_register_user)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"ProductManager", None))
        self.lbl_username.setText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.lbl_password.setText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.btn_register_user.setText(QCoreApplication.translate("MainWindow", u"REGISTER NOW", None))
        self.le_password.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Type your password", None))
        self.le_username.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Type your username", None))
        self.lbl_register.setText(QCoreApplication.translate("MainWindow", u"Register", None))
        self.lbl_username_7.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f ", None))
        self.cb_user_root.setItemText(0, QCoreApplication.translate("MainWindow", u"user", None))
        self.cb_user_root.setItemText(1, QCoreApplication.translate("MainWindow", u"moder", None))
        self.cb_user_root.setItemText(2, QCoreApplication.translate("MainWindow", u"admin", None))

    # retranslateUi

