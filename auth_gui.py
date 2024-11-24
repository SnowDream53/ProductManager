import sys
from PySide6 import QtWidgets
from PySide6.QtWidgets import QApplication, QMainWindow
from window.login_window import Ui_MainWindow
from database.connection_products import Data
from window import register_window
from main_gui import start_main_gui

class ProductManager_auth(QMainWindow):
    def __init__(self):
        super(ProductManager_auth, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.conn = Data()

        self.ui.btn_login.clicked.connect(self.login)
        self.ui.btn_signup.clicked.connect(self.open_register_window)

    def open_register_window(self):
        self.close()

        self.new_window_auth = QtWidgets.QMainWindow()
        self.ui_window_auth = register_window.Ui_MainWindow()
        self.ui_window_auth.setupUi(self.new_window_auth)
        self.ui_window_auth.btn_register.clicked.connect(self.check_register)

        self.new_window_auth.show()

    def check_register(self):
        if not self.conn.check_login_query(self.ui_window_auth.le_username.text()):
            if len(self.ui_window_auth.le_username.text()) > 0 and len(self.ui_window_auth.le_password.text()) > 0:
                if self.ui_window_auth.le_password.text() == self.ui_window_auth.le_confirm_password.text():
                    username = self.ui_window_auth.le_username.text()
                    password = self.ui_window_auth.le_confirm_password.text()

                    self.conn.register_user_query(username, password, "user")
                    QtWidgets.QMessageBox.about(self, "Регистрация", "Успешная регистрация аккаунта")

                    self.new_window_auth.close()
                    self.open_login_window()
                else:
                    QtWidgets.QMessageBox.about(self, "Регистрация", "Пароли не совпали")
                    self.new_window_auth.activateWindow()
                    self.new_window_auth.raise_()
            else:
                QtWidgets.QMessageBox.about(self, "Регистрация", "Введите данные")
                self.new_window_auth.activateWindow()
                self.new_window_auth.raise_()
        else:
            QtWidgets.QMessageBox.about(self, "Регистрация", "Логин уже занят")
            self.new_window_auth.activateWindow()
            self.new_window_auth.raise_()

    def open_login_window(self):
        self.auth_window = ProductManager_auth()
        self.auth_window.show()
        self.close()

    def login(self):
        if len(self.ui.le_username.text()) > 0 and len(self.ui.le_password.text()) > 0:
            if self.conn.login_user_query(self.ui.le_username.text(), self.ui.le_password.text()):
                self.open_main_window()
            else:
                QtWidgets.QMessageBox.about(self, "Авторизация", "Неверный логин или пароль")

    def open_main_window(self):
        start_main_gui(self.ui.le_username.text(), self.conn.get_user_group(self.ui.le_username.text()))
        self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ProductManager_auth()
    window.show()
    sys.exit(app.exec())
