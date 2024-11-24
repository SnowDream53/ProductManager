from PySide6 import QtWidgets, QtSql
import bcrypt

class Data:
    def __init__(self):
        super(Data, self).__init__()
        self.create_connection()

    def create_connection(self):
        db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('products.db')

        if not db.open():
            QtWidgets.QMessageBox.critical(None, "Не получилось открыть базу данных"
                                                 "Нажми на Cancel чтобы выйти.", QtWidgets.QMessageBox.Cancel)
            return False

        query = QtSql.QSqlQuery()
        if not query.exec("""
                CREATE TABLE IF NOT EXISTS products (
                    ID INTEGER PRIMARY KEY AUTOINCREMENT, 
                    Name VARCHAR(20), 
                    Category VARCHAR(20), 
                    Description VARCHAR(50), 
                    Price REAL, 
                    ExpirationDate DATE,
                    Action
                )
            """):
            QtWidgets.QMessageBox.critical(None, "Ошибка",
                                           "Не удалось создать таблицу products: " + query.lastError().text())
            return False

        if not query.exec("""
                CREATE TABLE IF NOT EXISTS accounts (
                    ID INTEGER PRIMARY KEY AUTOINCREMENT,
                    Username VARCHAR(20),
                    Password VARCHAR(20),
                    User_Group VARCHAR(10),
                    Action
                )
            """):
            QtWidgets.QMessageBox.critical(None, "Ошибка",
                                           "Не удалось создать таблицу accounts: " + query.lastError().text())
            return False

        return True

    def execute_query_with_params(self, sql_query, query_values):
        query = QtSql.QSqlQuery()
        query.prepare(sql_query)
        if query_values is not None:
            for query_value in query_values:
                query.addBindValue(query_value)
        if not query.exec():
            print("Ошибка выполнения запроса:", query.lastError().text())
        return query

    def add_new_product_query(self, name, category, description, price, date):
        try:
            sql_query = """
                INSERT INTO products (Name, Category, Description, Price, ExpirationDate)
                VALUES (?, ?, ?, ?, ?)
            """
            self.execute_query_with_params(sql_query, [name, category, description, price, date])
        except Exception as e:
            print(f"Ошибка в add_new_product_query: {e}")

    def update_product_query(self, name, category, description, price, date, id):
        sql_query = "UPDATE products SET Name=?, Category=?, Description=?, Price=?, ExpirationDate=? WHERE ID=?"
        self.execute_query_with_params(sql_query, [name, category, description, price, date, id])

    def delete_product_query(self, id):
        sql_query = "DELETE FROM products WHERE ID=?"
        self.execute_query_with_params(sql_query, [id])

    def get_product_query(self, id):
        sql_query = "SELECT Name, Category, Description, Price, ExpirationDate FROM products WHERE ID = ?"
        return self.execute_query_with_params(sql_query, [id])

    # Метод для добавления нового пользователя с хешированием пароля
    def register_user_query(self, username, password, group):
        password_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        password_hash_str = password_hash.decode('utf-8')

        sql_query = "INSERT INTO accounts (Username, Password, User_Group) VALUES (?,?,?)"
        self.execute_query_with_params(sql_query, [username, password_hash_str, group])

    # Метод для обновления данных пользователя
    def update_user_query(self, username, password, group, user_id):
        password_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        password_hash_str = password_hash.decode('utf-8')

        sql_query = "UPDATE accounts SET Username=?, Password=?, User_Group=? WHERE ID=?"
        self.execute_query_with_params(sql_query, [username, password_hash_str, group, user_id])

    # Метод для удаления пользователя
    def delete_user_query(self, user_id):
        sql_query = "DELETE FROM accounts WHERE ID=?"
        self.execute_query_with_params(sql_query, [user_id])

    # Метод для проверки существования пользователя по имени
    def check_login_query(self, username):
        sql_query = "SELECT 1 FROM accounts WHERE Username=?"
        query = self.execute_query_with_params(sql_query, [username])
        return query.next()

    # Метод для получения данных пользователя по ID
    def get_user_by_id(self, user_id):
        query = QtSql.QSqlQuery(f"SELECT Username, User_Group FROM accounts WHERE ID = {user_id}")
        if query.exec() and query.next():
            username = query.value(0)
            category = query.value(1)
            return username, category
        return None, None

    # Метод для проверки данных пользователя при входе
    def login_user_query(self, username, password):
        sql_query = "SELECT Password, User_Group FROM accounts WHERE Username=?"
        query = self.execute_query_with_params(sql_query, [username])

        if query.next():
            stored_password_hash = query.value(0)
            user_category = query.value(1)

            if bcrypt.checkpw(password.encode('utf-8'), stored_password_hash.encode('utf-8')):
                return user_category
        return None

    def get_user_group(self, username):
        sql_query = "SELECT User_Group FROM accounts WHERE Username=?"
        query = self.execute_query_with_params(sql_query, [username])
        if query and query.next():
            return query.value(0)
        else:
            return "user"
