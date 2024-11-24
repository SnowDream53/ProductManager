# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QStackedWidget,
    QTableView, QVBoxLayout, QWidget)
import window.res_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(857, 665)
        MainWindow.setMinimumSize(QSize(857, 665))
        MainWindow.setMaximumSize(QSize(857, 665))
        MainWindow.setStyleSheet(u"background-color: rgb(252, 252, 252);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setEnabled(True)
        self.stackedWidget.setGeometry(QRect(0, 80, 861, 601))
        self.stackedWidget.setMinimumSize(QSize(0, 0))
        self.stackedWidget.setAcceptDrops(False)
        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        self.layoutWidget = QWidget(self.page_1)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 10, 841, 571))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.product_top_frame = QFrame(self.layoutWidget)
        self.product_top_frame.setObjectName(u"product_top_frame")
        self.product_top_frame.setStyleSheet(u"background-color: rgba(255, 255, 255, 0.1);\n"
"border: 1.5px solid rgba(128, 128, 128, 40);\n"
"border-radius: 10px;")
        self.horizontalLayout_5 = QHBoxLayout(self.product_top_frame)
        self.horizontalLayout_5.setSpacing(6)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(12, 5, 12, 5)
        self.search_frame = QFrame(self.product_top_frame)
        self.search_frame.setObjectName(u"search_frame")
        self.search_frame.setStyleSheet(u"border: none;")
        self.horizontalLayout_3 = QHBoxLayout(self.search_frame)
        self.horizontalLayout_3.setSpacing(10)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(12, 12, 12, 12)
        self.le_search = QLineEdit(self.search_frame)
        self.le_search.setObjectName(u"le_search")
        self.le_search.setMaximumSize(QSize(180, 40))
        self.le_search.setStyleSheet(u"background-color: rgba(152, 159, 181, 20);\n"
"border: 1px solid rgba(152, 159, 181, 30);\n"
"border-radius: 8px;\n"
"\n"
"font-size: 14px;\n"
"color: black;\n"
"padding-left: 10px;")

        self.horizontalLayout_3.addWidget(self.le_search)

        self.cb_category = QComboBox(self.search_frame)
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
        self.cb_category.setMaximumSize(QSize(180, 40))
        self.cb_category.setStyleSheet(u"QComboBox {\n"
"background-color: rgba(152, 159, 181, 20);\n"
"border: 1px solid rgba(152, 159, 181, 30);\n"
"border-radius: 8px;\n"
"font-size: 14px;\n"
"color: black;\n"
"padding-left: 10px;\n"
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

        self.horizontalLayout_3.addWidget(self.cb_category)


        self.horizontalLayout_5.addWidget(self.search_frame)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_2)

        self.btn_add_update_frame = QFrame(self.product_top_frame)
        self.btn_add_update_frame.setObjectName(u"btn_add_update_frame")
        self.btn_add_update_frame.setStyleSheet(u"border: none;\n"
"")
        self.horizontalLayout_4 = QHBoxLayout(self.btn_add_update_frame)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.btn_add = QPushButton(self.btn_add_update_frame)
        self.btn_add.setObjectName(u"btn_add")
        self.btn_add.setMinimumSize(QSize(120, 0))
        self.btn_add.setStyleSheet(u"QPushButton {\n"
"color: #333;\n"
"font-size: 14px; \n"
"font-weight: bold;\n"
"\n"
"background-color: rgba(255, 255, 255, 0.7);\n"
"border: 1px solid rgba(128, 128, 128, 40);\n"
"border-radius: 8px;\n"
"padding: 8px 15px; \n"
"}\n"
"\n"
"QPushButton:hover {\n"
"border-color: rgba(128, 128, 128, 0.7);     \n"
"background-color: rgba(255, 255, 255, 0.85); \n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgba(200, 200, 200, 0.8); \n"
"}")

        self.horizontalLayout_4.addWidget(self.btn_add)

        self.btn_update = QPushButton(self.btn_add_update_frame)
        self.btn_update.setObjectName(u"btn_update")
        self.btn_update.setMinimumSize(QSize(120, 0))
        self.btn_update.setStyleSheet(u"QPushButton {\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5,\n"
"                                    stop:0 #00d4ff, stop:1 #ff00d4);\n"
"border-radius: 8px;\n"
"border: none;\n"
"padding: 8px;\n"
"color: white; \n"
"font-size: 14px;\n"
"font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(0, 122, 255, 0.9); \n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgba(0, 122, 255, 1.0); \n"
"}\n"
"")

        self.horizontalLayout_4.addWidget(self.btn_update)


        self.horizontalLayout_5.addWidget(self.btn_add_update_frame)


        self.verticalLayout.addWidget(self.product_top_frame)

        self.tableView_product = QTableView(self.layoutWidget)
        self.tableView_product.setObjectName(u"tableView_product")
        self.tableView_product.setStyleSheet(u"QTableView {\n"
"background-color: white;\n"
"border: 1px solid #e1e4e8;\n"
"gridline-color: #e1e4e8;\n"
"border-bottom-right-radius: 7px;\n"
"border-bottom-left-radius: 7px;\n"
"}\n"
"\n"
"QTableView::item {\n"
"padding: 8px;\n"
"border: none;\n"
"}\n"
"\n"
"QTableView::item::selected {\n"
"background-color: #f1f8ff;\n"
"color: #24292e;\n"
"}\n"
"\n"
"QTableView::section {\n"
"background-color: #f6f8fa;\n"
"padding: 8px;\n"
"border: none;\n"
"border-right: 1px solid #e1e4e8;\n"
"border-bottom: 1px solid #e1e4e8;\n"
"font-weight: bold;\n"
"color: #24292e;\n"
"}\n"
"\n"
"QHeaderView::section:first {\n"
"padding-left: 20px;\n"
"}\n"
"\n"
"QPushButton.edit-button {\n"
"background-color: #0366d6;\n"
"color: white;\n"
"border: none;\n"
"border-radius: 4px;\n"
"padding: 5px 15px;\n"
"min-width: 70px;\n"
"}\n"
"\n"
"QPushButton.delete-button {\n"
"background-color: #d73a49;\n"
"color: white;\n"
"border: none;\n"
"border-radius: 4px;\n"
"padding: 5px 15px;\n"
"min-width: 70px;\n"
"}\n"
"\n"
"QPushButton.edit-button:ho"
                        "ver {\n"
"background-color: #0357b8;\n"
"}\n"
"\n"
"QPushButton.delete-button:hover {\n"
"background-color: #cb2431;\n"
"}")

        self.verticalLayout.addWidget(self.tableView_product)

        self.stackedWidget.addWidget(self.page_1)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.tableView_users = QTableView(self.page_2)
        self.tableView_users.setObjectName(u"tableView_users")
        self.tableView_users.setGeometry(QRect(10, 80, 841, 501))
        self.tableView_users.setStyleSheet(u"QTableView {\n"
"background-color: white;\n"
"border: 1px solid #e1e4e8;\n"
"gridline-color: #e1e4e8;\n"
"selection-background-color: #f0f0f0;\n"
"border-bottom-right-radius: 7px;\n"
"border-bottom-left-radius: 7px;\n"
"}\n"
"\n"
"QTableView::item {\n"
"padding: 8px;\n"
"border-bottom: 1px solid #eee;\n"
"}\n"
"\n"
"QTableView::item::selected {\n"
"background-color: #e6f3ff;\n"
"color: black;\n"
"}\n"
"\n"
"QTableView::section {\n"
"background-color: #f6f8fa;\n"
"padding: 5px;\n"
"border: none;\n"
"border-right: 1px solid #e1e4e8;\n"
"border-bottom: 1px solid #e1e4e8;\n"
"font-weight: bold;\n"
"color: #24292e;\n"
"}\n"
"\n"
"QHeaderView::section:first {\n"
"padding-left: 20px;\n"
"}\n"
"\n"
"QPushButton.edit-button {\n"
"background-color: #0366d6;\n"
"color: white;\n"
"border: none;\n"
"border-radius: 4px;\n"
"padding: 5px 15px;\n"
"min-width: 70px;\n"
"}\n"
"\n"
"QPushButton.delete-button {\n"
"background-color: #d73a49;\n"
"color: white;\n"
"border: none;\n"
"border-radius: 4px;\n"
"padding: 5px 15px;\n"
"mi"
                        "n-width: 70px;\n"
"}\n"
"\n"
"QPushButton.edit-button:hover {\n"
"background-color: #0357b8;\n"
"}\n"
"\n"
"QPushButton.delete-button:hover {\n"
"background-color: #cb2431;\n"
"}\n"
"\n"
"QLabel[status=\"admin\"] {\n"
"    color: white;\n"
"    background-color: #007bff;\n"
"    border-radius: 10px;\n"
"    padding: 3px 10px;\n"
"}\n"
"\n"
"QLabel[status=\"moderator\"] {\n"
"    color: white;\n"
"    background-color: #6f42c1;\n"
"    border-radius: 10px;\n"
"    padding: 3px 10px;\n"
"}\n"
"\n"
"QLabel[status=\"user\"] {\n"
"    color: white;\n"
"    background-color: #6c757d;\n"
"    border-radius: 10px;\n"
"    padding: 3px 10px;\n"
"}")
        self.users_top_frame = QFrame(self.page_2)
        self.users_top_frame.setObjectName(u"users_top_frame")
        self.users_top_frame.setGeometry(QRect(10, 10, 841, 71))
        self.users_top_frame.setStyleSheet(u"background-color: rgba(255, 255, 255, 0.1);\n"
"border: 1.5px solid rgba(128, 128, 128, 40);\n"
"border-radius: 10px;")
        self.horizontalLayout_6 = QHBoxLayout(self.users_top_frame)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(12, 5, 12, 5)
        self.le_search_user = QLineEdit(self.users_top_frame)
        self.le_search_user.setObjectName(u"le_search_user")
        self.le_search_user.setMinimumSize(QSize(240, 40))
        self.le_search_user.setMaximumSize(QSize(240, 40))
        self.le_search_user.setStyleSheet(u"background-color: rgba(152, 159, 181, 20);\n"
"border: 1px solid rgba(152, 159, 181, 30);\n"
"border-radius: 8px;\n"
"\n"
"font-size: 14px;\n"
"color: black;\n"
"padding-left: 10px;")

        self.horizontalLayout_6.addWidget(self.le_search_user)

        self.cb_groups = QComboBox(self.users_top_frame)
        self.cb_groups.addItem("")
        self.cb_groups.addItem("")
        self.cb_groups.addItem("")
        self.cb_groups.addItem("")
        self.cb_groups.setObjectName(u"cb_groups")
        self.cb_groups.setMinimumSize(QSize(150, 40))
        self.cb_groups.setStyleSheet(u"QComboBox {\n"
"background-color: rgba(152, 159, 181, 20);\n"
"border: 1px solid rgba(152, 159, 181, 30);\n"
"border-radius: 8px;\n"
"font-size: 14px;\n"
"color: black;\n"
"padding-left: 10px;\n"
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

        self.horizontalLayout_6.addWidget(self.cb_groups)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_3)

        self.btn_update_2 = QPushButton(self.users_top_frame)
        self.btn_update_2.setObjectName(u"btn_update_2")
        self.btn_update_2.setMinimumSize(QSize(120, 0))
        self.btn_update_2.setStyleSheet(u"QPushButton {\n"
"color: #333;\n"
"font-size: 14px; \n"
"font-weight: bold;\n"
"\n"
"background-color: rgba(255, 255, 255, 0.7);\n"
"border: 1px solid rgba(128, 128, 128, 40);\n"
"border-radius: 8px;\n"
"padding: 8px 15px; \n"
"}\n"
"\n"
"QPushButton:hover {\n"
"border-color: rgba(128, 128, 128, 0.7);     \n"
"background-color: rgba(255, 255, 255, 0.85); \n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgba(200, 200, 200, 0.8); \n"
"}")

        self.horizontalLayout_6.addWidget(self.btn_update_2)

        self.btn_update_3 = QPushButton(self.users_top_frame)
        self.btn_update_3.setObjectName(u"btn_update_3")
        self.btn_update_3.setMinimumSize(QSize(120, 0))
        self.btn_update_3.setStyleSheet(u"QPushButton {\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5,\n"
"                                    stop:0 #00d4ff, stop:1 #ff00d4);\n"
"border-radius: 8px;\n"
"border: none;\n"
"padding: 8px;\n"
"color: white; \n"
"font-size: 14px;\n"
"font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(0, 122, 255, 0.9); \n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgba(0, 122, 255, 1.0); \n"
"}\n"
"")

        self.horizontalLayout_6.addWidget(self.btn_update_3)

        self.stackedWidget.addWidget(self.page_2)
        self.bottom_frame = QFrame(self.centralwidget)
        self.bottom_frame.setObjectName(u"bottom_frame")
        self.bottom_frame.setGeometry(QRect(10, 10, 841, 71))
        self.bottom_frame.setStyleSheet(u"background-color: rgba(255, 255, 255, 0.1);\n"
"border: 1.5px solid rgba(128, 128, 128, 40);\n"
"border-radius: 10px;")
        self.horizontalLayout_2 = QHBoxLayout(self.bottom_frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(12, 5, 12, 5)
        self.btn_frame = QFrame(self.bottom_frame)
        self.btn_frame.setObjectName(u"btn_frame")
        self.btn_frame.setStyleSheet(u"border: none;")
        self.horizontalLayout = QHBoxLayout(self.btn_frame)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_product = QPushButton(self.btn_frame)
        self.btn_product.setObjectName(u"btn_product")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_product.sizePolicy().hasHeightForWidth())
        self.btn_product.setSizePolicy(sizePolicy)
        self.btn_product.setMinimumSize(QSize(100, 30))
        self.btn_product.setStyleSheet(u"QPushButton {\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5,\n"
"                                    stop:0 #00d4ff, stop:1 #ff00d4);\n"
"border-radius: 8px;\n"
"border: none;\n"
"padding: 8px;\n"
"color: white; \n"
"font-size: 14px;\n"
"font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(0, 122, 255, 0.9); \n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgba(0, 122, 255, 1.0); \n"
"}\n"
"")

        self.horizontalLayout.addWidget(self.btn_product)

        self.btn_users = QPushButton(self.btn_frame)
        self.btn_users.setObjectName(u"btn_users")
        self.btn_users.setMinimumSize(QSize(0, 0))
        self.btn_users.setMaximumSize(QSize(170, 37))
        self.btn_users.setStyleSheet(u"QPushButton {\n"
"color: #333;\n"
"font-size: 14px; \n"
"font-weight: bold;\n"
"\n"
"background-color: rgba(255, 255, 255, 0.7);\n"
"border: 1px solid rgba(128, 128, 128, 40);\n"
"border-radius: 8px;\n"
"padding: 8px 15px; \n"
"}\n"
"\n"
"QPushButton:hover {\n"
"border-color: rgba(128, 128, 128, 0.7);     \n"
"background-color: rgba(255, 255, 255, 0.85); \n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgba(200, 200, 200, 0.8); \n"
"}")

        self.horizontalLayout.addWidget(self.btn_users)


        self.horizontalLayout_2.addWidget(self.btn_frame)

        self.horizontalSpacer = QSpacerItem(300, 0, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.user_frame_2 = QFrame(self.bottom_frame)
        self.user_frame_2.setObjectName(u"user_frame_2")
        self.user_frame_2.setStyleSheet(u"border: none;\n"
"\n"
"")
        self.user_frame = QHBoxLayout(self.user_frame_2)
        self.user_frame.setSpacing(0)
        self.user_frame.setObjectName(u"user_frame")
        self.user_frame.setContentsMargins(8, 8, 8, 8)
        self.lbl_icon_user = QLabel(self.user_frame_2)
        self.lbl_icon_user.setObjectName(u"lbl_icon_user")
        self.lbl_icon_user.setMaximumSize(QSize(24, 24))
        self.lbl_icon_user.setStyleSheet(u"background-color: none;\n"
"border: none;\n"
"")
        self.lbl_icon_user.setPixmap(QPixmap(u":/icons/icons/person_black.svg"))

        self.user_frame.addWidget(self.lbl_icon_user)

        self.lbl_category_user = QLabel(self.user_frame_2)
        self.lbl_category_user.setObjectName(u"lbl_category_user")
        self.lbl_category_user.setStyleSheet(u"color: black;\n"
"font-size: 14px;\n"
"background-color: none;\n"
"border: none;\n"
"font-weigth: bold;")

        self.user_frame.addWidget(self.lbl_category_user)

        self.lbl_username = QLabel(self.user_frame_2)
        self.lbl_username.setObjectName(u"lbl_username")
        self.lbl_username.setStyleSheet(u"color: black;\n"
"font-size: 14px;\n"
"background-color: none;\n"
"border: none;\n"
"font-weigth: bold;")

        self.user_frame.addWidget(self.lbl_username)


        self.horizontalLayout_2.addWidget(self.user_frame_2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"ProductManager", None))
        self.le_search.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0438\u0441\u043a...", None))
        self.cb_category.setItemText(0, "")
        self.cb_category.setItemText(1, QCoreApplication.translate("MainWindow", u"\u0424\u0440\u0443\u043a\u0442\u044b", None))
        self.cb_category.setItemText(2, QCoreApplication.translate("MainWindow", u"\u041e\u0432\u043e\u0449\u0438", None))
        self.cb_category.setItemText(3, QCoreApplication.translate("MainWindow", u"\u0421\u043b\u0430\u0434\u043e\u0441\u0442\u0438", None))
        self.cb_category.setItemText(4, QCoreApplication.translate("MainWindow", u"\u041c\u043e\u043b\u043e\u0447\u043d\u044b\u0435 \u0442\u043e\u0432\u0430\u0440\u044b", None))
        self.cb_category.setItemText(5, QCoreApplication.translate("MainWindow", u"\u041c\u044f\u0441\u043e", None))
        self.cb_category.setItemText(6, QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043c\u043e\u0440\u043e\u0437\u043a\u0430", None))
        self.cb_category.setItemText(7, QCoreApplication.translate("MainWindow", u"\u0411\u0430\u043a\u0430\u043b\u0435\u044f", None))
        self.cb_category.setItemText(8, QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043b\u0431\u0430\u0441\u043d\u044b\u0435 \u0438\u0437\u0434\u0435\u043b\u0438\u044f", None))

        self.cb_category.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f", None))
        self.btn_add.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.btn_update.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u043d\u043e\u0432\u0438\u0442\u044c", None))
        self.le_search_user.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0438\u0441\u043a \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f...", None))
        self.cb_groups.setItemText(0, "")
        self.cb_groups.setItemText(1, QCoreApplication.translate("MainWindow", u"user", None))
        self.cb_groups.setItemText(2, QCoreApplication.translate("MainWindow", u"moder", None))
        self.cb_groups.setItemText(3, QCoreApplication.translate("MainWindow", u"admin", None))

        self.cb_groups.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0413\u0440\u0443\u043f\u043f\u0430", None))
        self.btn_update_2.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.btn_update_3.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u043d\u043e\u0432\u0438\u0442\u044c", None))
        self.btn_product.setText(QCoreApplication.translate("MainWindow", u"\u0422\u043e\u0432\u0430\u0440\u044b", None))
        self.btn_users.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u0438", None))
        self.lbl_icon_user.setText("")
        self.lbl_category_user.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044c:", None))
        self.lbl_username.setText(QCoreApplication.translate("MainWindow", u"Username", None))
    # retranslateUi

