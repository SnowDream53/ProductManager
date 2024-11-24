# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_product.ui'
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
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QComboBox, QDateEdit,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(379, 577)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(379, 577))
        MainWindow.setMaximumSize(QSize(379, 577))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 30, 359, 67))
        self.label.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label.setStyleSheet(u"color: #1A1B1F;\n"
"font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;\n"
"font-size: 32px;\n"
"font-weight: 600;\n"
"letter-spacing: -0.5px;\n"
"margin-bottom: 24px;\n"
"text-align: left;\n"
"padding: 0;\n"
"line-height: 1.3;\n"
"border: none;")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lbl_username_6 = QLabel(self.centralwidget)
        self.lbl_username_6.setObjectName(u"lbl_username_6")
        self.lbl_username_6.setGeometry(QRect(40, 110, 101, 21))
        self.lbl_username_6.setStyleSheet(u"font-size: 12px;\n"
"color: #444;")
        self.le_name = QLineEdit(self.centralwidget)
        self.le_name.setObjectName(u"le_name")
        self.le_name.setGeometry(QRect(40, 130, 311, 41))
        self.le_name.setStyleSheet(u"border: none;\n"
"border-bottom: 1px solid #444;\n"
"font-size: 14px;\n"
"color: #444;\n"
"padding: 5px;\n"
"\n"
"")
        self.lbl_username_7 = QLabel(self.centralwidget)
        self.lbl_username_7.setObjectName(u"lbl_username_7")
        self.lbl_username_7.setGeometry(QRect(40, 180, 101, 21))
        self.lbl_username_7.setStyleSheet(u"font-size: 12px;\n"
"color: #444;")
        self.le_description = QLineEdit(self.centralwidget)
        self.le_description.setObjectName(u"le_description")
        self.le_description.setGeometry(QRect(40, 270, 311, 41))
        self.le_description.setStyleSheet(u"border: none;\n"
"border-bottom: 1px solid #444;\n"
"font-size: 14px;\n"
"color: #444;\n"
"padding: 5px;\n"
"\n"
"")
        self.lbl_username_8 = QLabel(self.centralwidget)
        self.lbl_username_8.setObjectName(u"lbl_username_8")
        self.lbl_username_8.setGeometry(QRect(40, 250, 101, 21))
        self.lbl_username_8.setStyleSheet(u"font-size: 12px;\n"
"color: #444;")
        self.le_price = QLineEdit(self.centralwidget)
        self.le_price.setObjectName(u"le_price")
        self.le_price.setGeometry(QRect(40, 340, 311, 41))
        self.le_price.setStyleSheet(u"border: none;\n"
"border-bottom: 1px solid #444;\n"
"font-size: 14px;\n"
"color: #444;\n"
"padding: 5px;\n"
"\n"
"")
        self.lbl_username_9 = QLabel(self.centralwidget)
        self.lbl_username_9.setObjectName(u"lbl_username_9")
        self.lbl_username_9.setGeometry(QRect(40, 320, 101, 21))
        self.lbl_username_9.setStyleSheet(u"font-size: 12px;\n"
"color: #444;")
        self.lbl_username_10 = QLabel(self.centralwidget)
        self.lbl_username_10.setObjectName(u"lbl_username_10")
        self.lbl_username_10.setGeometry(QRect(40, 390, 101, 21))
        self.lbl_username_10.setStyleSheet(u"font-size: 12px;\n"
"color: #444;")
        self.dateEdit = QDateEdit(self.centralwidget)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setGeometry(QRect(40, 410, 311, 41))
        self.dateEdit.setStyleSheet(u"border: none;\n"
"border-bottom: 1px solid #444;\n"
"font-size: 14px;\n"
"color: #444;\n"
"padding: 5px;\n"
"\n"
"")
        self.dateEdit.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.dateEdit.setDateTime(QDateTime(QDate(2023, 12, 31), QTime(4, 0, 0)))
        self.btn_add = QPushButton(self.centralwidget)
        self.btn_add.setObjectName(u"btn_add")
        self.btn_add.setGeometry(QRect(20, 520, 341, 41))
        self.btn_add.setStyleSheet(u"QPushButton {\n"
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
        self.cb_category = QComboBox(self.centralwidget)
        self.cb_category.addItem("")
        self.cb_category.addItem("")
        self.cb_category.addItem("")
        self.cb_category.addItem("")
        self.cb_category.addItem("")
        self.cb_category.addItem("")
        self.cb_category.addItem("")
        self.cb_category.addItem("")
        self.cb_category.addItem("")
        self.cb_category.setObjectName(u"cb_category")
        self.cb_category.setGeometry(QRect(40, 200, 311, 41))
        self.cb_category.setStyleSheet(u"QComboBox {\n"
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
        QWidget.setTabOrder(self.le_name, self.cb_category)
        QWidget.setTabOrder(self.cb_category, self.le_description)
        QWidget.setTabOrder(self.le_description, self.le_price)
        QWidget.setTabOrder(self.le_price, self.dateEdit)
        QWidget.setTabOrder(self.dateEdit, self.btn_add)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"ProductManager", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u043b\u0435\u043d\u0438\u0435 \u0442\u043e\u0432\u0430\u0440\u0430", None))
        self.lbl_username_6.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0442\u043e\u0432\u0430\u0440\u0430", None))
        self.le_name.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0442\u043e\u0432\u0430\u0440\u0430", None))
        self.lbl_username_7.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f ", None))
        self.le_description.setText("")
        self.le_description.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435", None))
        self.lbl_username_8.setText(QCoreApplication.translate("MainWindow", u"\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435", None))
        self.le_price.setText("")
        self.le_price.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0426\u0435\u043d\u0430 \u0442\u043e\u0432\u0430\u0440\u0430", None))
        self.lbl_username_9.setText(QCoreApplication.translate("MainWindow", u"\u0426\u0435\u043d\u0430", None))
        self.lbl_username_10.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0440\u043e\u043a \u0433\u043e\u0434\u043d\u043e\u0441\u0442\u0438", None))
        self.btn_add.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0442\u043e\u0432\u0430\u0440", None))
        self.cb_category.setItemText(0, "")
        self.cb_category.setItemText(1, QCoreApplication.translate("MainWindow", u"\u0424\u0440\u0443\u043a\u0442\u044b", None))
        self.cb_category.setItemText(2, QCoreApplication.translate("MainWindow", u"\u041e\u0432\u043e\u0449\u0438", None))
        self.cb_category.setItemText(3, QCoreApplication.translate("MainWindow", u"\u0421\u043b\u0430\u0434\u043e\u0441\u0442\u0438", None))
        self.cb_category.setItemText(4, QCoreApplication.translate("MainWindow", u"\u041c\u043e\u043b\u043e\u0447\u043d\u044b\u0435 \u0442\u043e\u0432\u0430\u0440\u044b", None))
        self.cb_category.setItemText(5, QCoreApplication.translate("MainWindow", u"\u041c\u044f\u0441\u043e", None))
        self.cb_category.setItemText(6, QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043c\u043e\u0440\u043e\u0437\u043a\u0430", None))
        self.cb_category.setItemText(7, QCoreApplication.translate("MainWindow", u"\u0411\u0430\u043a\u0430\u043b\u0435\u044f", None))
        self.cb_category.setItemText(8, QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043b\u0431\u0430\u0441\u043d\u044b\u0435 \u0438\u0437\u0434\u0435\u043b\u0438\u044f", None))

    # retranslateUi

