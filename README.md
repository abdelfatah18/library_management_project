# 📚 Library Management System API

## 🚀 Project Overview
The **Library Management System API** is a backend service built with **Django** and **Django REST Framework (DRF)**. It allows users to manage library resources by **borrowing, returning, and viewing books**. This project follows **RESTful principles** and supports user authentication.

## 🛠 Features
- 📖 **Books Management (CRUD)**
  - Add, view, update, and delete books.
  - Each book has a **title, author, ISBN, published date, and number of copies available**.
  - Ensures **ISBN uniqueness**.

- 👤 **Users Management (CRUD)**
  - Register and manage users with **username, email, and membership date**.
  - Users have an **active status**.

- 🔄 **Borrow & Return Books**
  - Users can **check out books** if copies are available.
  - Book count updates on checkout/return.
  - Keeps track of **borrowing and return dates**.

- 🔍 **View Available Books**
  - List all books.
  - Filter books by **title, author, or ISBN**.

## 🛠 Tech Stack
- **Backend:** Django, Django REST Framework
- **Database:** PostgreSQL / SQLite
- **Authentication:** Django’s built-in authentication
- **Deployment:** Heroku / PythonAnywhere (Optional)
- **API Testing:** Postman, DRF Browsable API

## 📂 Project Setup
### 1️⃣ Clone the Repository  
```bash
git clone https://github.com/abdelfatah18/Alx_DjangoLearnLab.git
cd Alx_DjangoLearnLab/django-models/LibraryProject
