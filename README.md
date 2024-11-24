# Product Manager / Менеджер Товаров

**Product Manager** is a desktop application for managing products and users. It allows users to add, edit, and delete products, as well as manage user accounts with different access levels (admin, moderator, user).

**Менеджер Товаров** — это настольное приложение для управления товарами и пользователями. Оно предоставляет возможность добавления, редактирования и удаления товаров, а также управления учетными записями пользователей с различными уровнями доступа (администратор, модератор, пользователь).

---

## 🛠️ Features / Основные возможности

### Product Management / Управление товарами:
- Add new products with name, category, description, price, and expiration date.
- Search and filter products by name and category.
- Edit product details.
- Delete products.

- Добавление новых товаров с указанием имени, категории, описания, цены и срока годности.
- Поиск и фильтрация товаров по имени и категории.
- Редактирование информации о товарах.
- Удаление товаров.

### User Management / Управление пользователями:
- Add new users with role (admin, moderator, user).
- Edit user accounts (admins only).
- Delete user accounts.
- Restrict editing for active users.

- Добавление новых пользователей с определением их группы (admin, moder, user).
- Редактирование учетных записей пользователей (доступно только для администраторов).
- Удаление учетных записей.
- Ограничение редактирования для активных пользователей.

### Access Control / Разграничение доступа:
- **Admin:** Full access to manage products and users.
- **Moderator:** Full access to manage products, restricted from managing users.
- **User:** View-only access.

- **Администратор:** Полный доступ к управлению товарами и пользователями.
- **Модератор:** Полный доступ к товарам, но без возможности управления пользователями.
- **Пользователь:** Только просмотр.

---

## 💻 Requirements / Требования

To run the application, you need:  
Для работы приложения требуется:  
- Python 3.8+
- Libraries / Библиотеки:
  - PySide6
  - PyQt5 (for icons if using Qt Designer / для иконок, если используется Qt Designer)
  - PyInstaller (for building `.exe` files / для сборки `.exe` файлов)

---

## 📦 Installation / Установка

### Clone the repository / Клонировать репозиторий:
```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY_NAME.git
cd YOUR_REPOSITORY_NAME
