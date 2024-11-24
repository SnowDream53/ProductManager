import sys
from PySide6 import QtWidgets, QtCore, QtSql, QtGui
from PySide6.QtWidgets import QApplication, QMainWindow, QTableView, QVBoxLayout, QWidget, QPushButton, QHBoxLayout
from PySide6.QtCore import QDate
from window import add_product_window
from window import add_new_user_window
from window.ui_main import Ui_MainWindow
from database.connection_products import Data
from datetime import datetime


class ProductManager(QMainWindow):
    def __init__(self, username, group):
        super(ProductManager, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.conn = Data()
        self.group = group

        self.model = None
        self.model_users = None

        self.ui.lbl_username.setText(username)
        self.ui.btn_product.clicked.connect(self.show_product_page)
        self.ui.btn_users.clicked.connect(self.show_users_page)

        self.current_page = 'products'
        self.show_product_page()

        self.setup_signals()

    def setup_signals(self):
        # Товары
        self.ui.btn_add.clicked.connect(self.open_add_product_window)
        self.ui.btn_update.clicked.connect(self.view_data_products)
        self.ui.le_search.textChanged.connect(lambda: self.apply_filters() if self.current_page == 'products' else None)
        self.ui.cb_category.currentIndexChanged.connect(lambda: self.apply_filters() if self.current_page == 'products' else None)

        # Пользователи
        self.ui.btn_update_2.clicked.connect(self.open_add_user_window)
        self.ui.btn_update_3.clicked.connect(self.view_users_data)
        self.ui.le_search_user.textChanged.connect(
            lambda: self.apply_user_filters() if self.current_page == 'users' else None)
        self.ui.cb_groups.currentIndexChanged.connect(
            lambda: self.apply_user_filters() if self.current_page == 'users' else None)

    def cleanup_model(self):
        # Очистка старой модели
        if self.model is not None:
            self.model.clear()
            self.model = None
        if self.model_users is not None:
            self.model_users.clear()
            self.model_users = None

    def reset_completers(self):
        # Отключение и очистка комплитеров
        for widget in [self.ui.le_search, self.ui.cb_category,
                      self.ui.le_search_user, self.ui.cb_groups]:
            if widget.completer():
                completer = widget.completer()
                widget.setCompleter(None)
                completer.deleteLater()
            widget.clear()

    def fill_comboboxes(self):
        if self.current_page == 'products':
            categories = ["", "Фрукты", "Овощи", "Сладости", "Молочные товары", "Мясо", "Заморозка", "Бакалея",
                          "Колбасные изделия"]
            self.ui.cb_category.addItems(categories)
        elif self.current_page == 'users':
            user_groups = ["", "user", "moder", "admin"]
            self.ui.cb_groups.addItems(user_groups)

    def set_user_access(self):
        # Проверяем, какой у пользователя доступ
        if self.group == "admin":
            # Администратор может видеть все кнопки
            self.ui.btn_users.setVisible(True)
            self.ui.btn_add.setVisible(True)
            # Скрывать столбец Action для всех
            if self.model is not None and self.model.columnCount() > 6:
                self.ui.tableView_product.setColumnHidden(self.model.columnCount() - 1, False)

        elif self.group == "moder":
            # Модератор может видеть все, кроме добавления пользователей
            self.ui.btn_users.setVisible(False)  # Модератор не может добавлять пользователей
            self.ui.btn_add.setVisible(True)  # Модератор может добавлять продукты
            # Скрывать столбец Action для всех
            if self.model is not None and self.model.columnCount() > 6:
                self.ui.tableView_product.setColumnHidden(self.model.columnCount() - 1, False)

        else:
            # Для остальных групп, например, обычных пользователей
            self.ui.btn_users.setVisible(False)
            self.ui.btn_add.setVisible(False)
            # Скрываем все действия
            if self.model is not None and self.model.columnCount() > 6:
                self.ui.tableView_product.setColumnHidden(self.model.columnCount() - 1, True)

    def show_product_page(self):
        QtCore.QTimer.singleShot(0, self._show_product_page)

    def _show_product_page(self):
        self.current_page = 'products'
        self.cleanup_model()
        self.reset_completers()
        self.fill_comboboxes()
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_1)
        self.view_data_products()

    def view_data_products(self):
        if self.model is None:
            self.model = QtSql.QSqlTableModel(self)
            self.model.setTable("products")
        self.model.select()

        self.ui.tableView_product.setModel(self.model)
        self.set_column_widths()

        QtCore.QTimer.singleShot(100, self.set_user_access)

        for row in range(self.model.rowCount()):
            self.add_action_buttons(row)

    def set_column_widths(self):
        self.ui.tableView_product.setColumnWidth(0, 60)
        self.ui.tableView_product.setColumnWidth(1, 100)
        self.ui.tableView_product.setColumnWidth(2, 145)
        self.ui.tableView_product.setColumnWidth(3, 145)
        self.ui.tableView_product.setColumnWidth(4, 100)
        self.ui.tableView_product.setColumnWidth(5, 150)

    def add_action_buttons(self, row):
        product_id = self.model.record(row).value("ID")

        edit_button_products = QtWidgets.QPushButton("✏️")
        edit_button_products.clicked.connect(lambda checked, id=product_id: self.edit_product(id))
        edit_button_products.setStyleSheet("background: transparent; border: none;")

        delete_button_products = QtWidgets.QPushButton("❌")
        delete_button_products.clicked.connect(lambda checked, id=product_id: self.delete_product(id))
        delete_button_products.setStyleSheet("background: transparent; border: none;")

        action_widget = QtWidgets.QWidget()
        action_layout = QtWidgets.QHBoxLayout(action_widget)
        action_layout.addWidget(edit_button_products)
        action_layout.addWidget(delete_button_products)
        action_layout.setContentsMargins(0, 0, 0, 0)

        self.ui.tableView_product.setIndexWidget(self.model.index(row, self.model.columnCount() - 1), action_widget)

    def open_add_product_window(self):
        self.new_window = QtWidgets.QMainWindow()
        self.ui_window = add_product_window.Ui_MainWindow()
        self.ui_window.setupUi(self.new_window)

        self.new_window.show()

        self.ui_window.btn_add.clicked.connect(self.add_product)

    def add_product(self):
        name = self.ui_window.le_name.text()
        category = self.ui_window.cb_category.currentText()
        description = self.ui_window.le_description.text()

        try:
            price = float(self.ui_window.le_price.text().strip())
        except ValueError:
            QtWidgets.QMessageBox.warning(self, "ProductManager", "Цена должна быть числом")

        date = datetime.strptime(self.ui_window.dateEdit.date().toString("dd.MM.yyyy"), "%d.%m.%Y").strftime("%Y-%m-%d")

        self.conn.add_new_product_query(name, category, description, price, date)
        self.view_data_products()
        self.new_window.close()

    def edit_product(self, product_id):
        query = self.conn.get_product_query(product_id)

        if query.exec():
            if query.next():
                name = query.value(0)
                category = query.value(1)
                description = query.value(2)
                price = query.value(3)

                try:
                    expiration_date = datetime.strptime(query.value(4), "%Y-%m-%d").strftime("%d.%m.%Y")
                except ValueError:
                    expiration_date = ""

                self.new_window = QtWidgets.QMainWindow()
                self.ui_window = add_product_window.Ui_MainWindow()
                self.ui_window.setupUi(self.new_window)

                self.ui_window.le_name.setText(name)
                self.ui_window.cb_category.setCurrentText(category)
                self.ui_window.le_description.setText(description)
                self.ui_window.le_price.setText(str(price))
                self.ui_window.dateEdit.setDate(QDate.fromString(expiration_date, "dd.MM.yyyy"))

                self.ui_window.label.setText("Обновить продукт")
                self.ui_window.btn_add.setText("Обновить")
                self.ui_window.btn_add.clicked.connect(lambda: self.update_product(product_id))

                self.new_window.show()

    def update_product(self, product_id):
        name = self.ui_window.le_name.text()
        category = self.ui_window.cb_category.currentText()
        description = self.ui_window.le_description.text()
        date = datetime.strptime(self.ui_window.dateEdit.date().toString("dd.MM.yyyy"), "%d.%m.%Y").strftime("%Y-%m-%d")

        try:
            price = float(self.ui_window.le_price.text().strip())
        except ValueError:
            QtWidgets.QMessageBox.warning(self, "ProductManager", "Цена должна быть числом")

        self.conn.update_product_query(name, category, description, price, date, product_id)
        self.view_data_products()
        self.new_window.close()

    def delete_product(self, product_id):
        self.conn.delete_product_query(product_id)
        self.view_data_products()

    def apply_filters(self):
        if self.model and self.current_page == 'products':
            search_text = self.ui.le_search.text().strip()
            category = self.ui.cb_category.currentText().strip()

            filter_str_products = ""

            if search_text:
                filter_str_products += f"Name LIKE '{search_text}%'"

            if category:
                if filter_str_products:
                    filter_str_products += " AND "
                filter_str_products += f"Category LIKE '{category}%'"

            self.model.setFilter(filter_str_products)

    def setup_search_autocomplete(self):
        query = QtSql.QSqlQuery("SELECT DISTINCT Name FROM products")
        names = []
        while query.next():
            names.append(query.value(0))

        completer_products = QtWidgets.QCompleter(names)
        self.ui.le_search.setCompleter(completer_products)

    def setup_category_autocomplete(self):
        query = QtSql.QSqlQuery("SELECT DISTINCT Category FROM products")
        categories = []
        while query.next():
            categories.append(query.value(0))

        completer_products = QtWidgets.QCompleter(categories)
        self.ui.cb_category.setCompleter(completer_products)

    def show_users_page(self):
        QtCore.QTimer.singleShot(0, self._show_users_page)

    def _show_users_page(self):
        self.current_page = 'users'
        self.cleanup_model()
        self.reset_completers()
        self.fill_comboboxes()
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_2)
        self.view_users_data()

    def view_users_data(self):
        if self.model_users is None:
            self.model_users = QtSql.QSqlTableModel(self)
            self.model_users.setTable("accounts")

        self.model_users.select()
        self.ui.tableView_users.setModel(self.model_users)
        self.set_user_column_widths()

        QtCore.QTimer.singleShot(100, self.setup_user_completers)

        for row in range(self.model_users.rowCount()):
            self.add_user_action_buttons(row)

    def setup_user_completers(self):
        if self.current_page == 'users':
            self.setup_user_search_autocomplete()
            self.setup_user_groups_autocomplete()

    def set_user_column_widths(self):
        self.ui.tableView_users.setColumnWidth(0, 60)
        self.ui.tableView_users.setColumnWidth(1, 250)
        self.ui.tableView_users.setColumnWidth(2, 250)
        self.ui.tableView_users.setColumnWidth(3, 140)

    def add_user_action_buttons(self, row):
        user_id = self.model_users.record(row).value("ID")

        edit_button_users = QtWidgets.QPushButton("✏️")
        edit_button_users.clicked.connect(lambda checked, id=user_id: self.edit_user(id))
        edit_button_users.setStyleSheet("background: transparent; border: none;")

        delete_button_users = QtWidgets.QPushButton("❌")
        delete_button_users.clicked.connect(lambda checked, id=user_id: self.delete_user(id))
        delete_button_users.setStyleSheet("background: transparent; border: none;")

        action_widget = QtWidgets.QWidget()
        action_layout = QtWidgets.QHBoxLayout(action_widget)
        action_layout.addWidget(edit_button_users)
        action_layout.addWidget(delete_button_users)
        action_layout.setContentsMargins(0, 0, 0, 0)

        self.ui.tableView_users.setIndexWidget(self.model_users.index(row, self.model_users.columnCount() - 1), action_widget)

    def open_add_user_window(self):
        self.new_window_user = QtWidgets.QMainWindow()
        self.ui_window_user = add_new_user_window.Ui_MainWindow()
        self.ui_window_user.setupUi(self.new_window_user)

        self.ui_window_user.btn_register_user.clicked.connect(self.add_user)

        self.new_window_user.show()

    def add_user(self):
        username = self.ui_window_user.le_username.text()
        password = self.ui_window_user.le_password.text()
        group = self.ui_window_user.cb_user_root.currentText()

        if self.conn.check_login_query(username):
            QtWidgets.QMessageBox.warning(self, "Ошибка", "Пользователь с таким именем уже существует.")
            self.new_window_user.activateWindow()
            self.new_window_user.raise_()
            return

        self.conn.register_user_query(username, password, group)
        self.view_users_data()
        self.new_window_user.close()

    def edit_user(self, user_id):
        username, category = self.conn.get_user_by_id(user_id)

        self.new_window_user = QtWidgets.QMainWindow()
        self.ui_window_user = add_new_user_window.Ui_MainWindow()
        self.ui_window_user.setupUi(self.new_window_user)

        self.ui_window_user.le_username.setText(username)
        self.ui_window_user.cb_user_root.setCurrentText(category)

        self.ui_window_user.lbl_register.setText("Обновить пользователя")
        self.ui_window_user.btn_register_user.setText("Обновить")
        self.ui_window_user.btn_register_user.clicked.connect(lambda: self.update_user(user_id))

        self.new_window_user.show()

    def update_user(self, user_id):
        username = self.ui_window_user.le_username.text()
        password = self.ui_window_user.le_password.text()
        group = self.ui_window_user.cb_user_root.currentText()

        self.conn.update_user_query(username, password, group, user_id)
        self.view_users_data()
        self.new_window_user.close()

    def delete_user(self, user_id):
        self.conn.delete_user_query(user_id)
        self.view_users_data()

    def apply_user_filters(self):
        if self.model_users and self.current_page == 'users':
            search_text = self.ui.le_search_user.text().strip()
            group = self.ui.cb_groups.currentText().strip()

            filter_str_user = ""

            if search_text:
                filter_str_user += f"Username LIKE '{search_text}%'"

            if group:
                if filter_str_user:
                    filter_str_user += " AND "
                filter_str_user += f"User_Group LIKE '{group}%'"

            self.model_users.setFilter(filter_str_user)

    def setup_user_search_autocomplete(self):
        query = QtSql.QSqlQuery("SELECT DISTINCT Username FROM accounts")
        usernames = []
        while query.next():
            usernames.append(query.value(0))

        completer_user = QtWidgets.QCompleter(usernames)
        self.ui.le_search_user.setCompleter(completer_user)

    def setup_user_groups_autocomplete(self):
        query = QtSql.QSqlQuery("SELECT DISTINCT User_Group FROM accounts")
        categories = []
        while query.next():
            categories.append(query.value(0))

        completer_user = QtWidgets.QCompleter(categories)
        self.ui.cb_groups.setCompleter(completer_user)

def start_main_gui(username, group):
    window = ProductManager(username, group)
    window.show()

    return window