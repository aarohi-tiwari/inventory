# Inventory Management System 

A clean and production-ready Inventory Management System built using:

- Django
- Django REST Framework
- Bootstrap 5
- SQLite (default)
- Virtual Environment
- Pagination
- Custom Error Handling

---

## Features

### Backend (API)
- Create Product
- Fetch Single Product
- Fetch Paginated Product List
- Update Product
- Delete Product
- Custom Pagination
- Structured Error Responses
- Field Validations

### Frontend (UI)
- Modern Bootstrap Dashboard
- Product List View
- Create / Edit Form
- Delete Confirmation
- Flash Success Messages
- Responsive Layout

---

## Project Structure
inventory_project/
│
├── inventory/ # Project configuration
├── products/ # Main app
├── templates/ # UI templates
├── venv/ # Virtual environment
├── manage.py
├── requirements.txt
└── README.md


---

# ⚙️ Setup Instructions

## 1️⃣ Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/inventory-api.git
cd inventory-api
```

### 2️⃣ Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate #MAC
venv\Scripts\activate #WINDOWS
```
### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Run Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5️⃣ Run Server
```bash
python manage.py runserver
```
Server runs at: http://127.0.0.1:8000/
API Endpoints : http://127.0.0.1:8000/api/

| Method | Endpoint        | Description               |
| ------ | --------------- | ------------------------- |
| POST   | /products/      | Create product            |
| GET    | /products/      | List products (paginated) |
| GET    | /products/{id}/ | Retrieve product          |
| PUT    | /products/{id}/ | Update product            |
| DELETE | /products/{id}/ | Delete product            |

UI Access :
http://127.0.0.1:8000/api/ui/products/

**UI Features:**
Add Product
Edit Product
Delete Product
Pagination (if enabled)
Responsive Bootstrap design

**Validations Implemented**
Price must be > 0
Quantity cannot be negative
Required fields enforced
Structured error messages

**Technologies Used**
Python 3.x
Django
Django REST Framework
Bootstrap 5
SQLite
