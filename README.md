# 🛋️ Wayfair Clone (Django E-commerce Project)

A work-in-progress full-stack e-commerce website built with Django, inspired by Wayfair.  
This project is designed to mimic a modern online store, focusing on user experience, clean structure, and modular code.

## ✅ Features Implemented So Far

- 🏠 **Home Page**: Fully responsive with dynamic navigation and product categories.
- 🛍️ **Shop Page**: Displays a list of products with pagination, category filtering, and product counts.
- 🔍 **Search**: Search bar in the navbar to find products by name.
- 🛒 **Product Detail Page**: View detailed information with additional images and related items.
- 👤 **User Authentication**:
  - Signup and login using Django's default system (username + password).
  - Navbar dynamically updates based on user authentication status.

## 🗂️ Project Structure

- `main/` – Static pages and common components (navbar, footer, etc.).
- `products/` – Handles all product-related models, views, and templates.
- `users/` – Manages user registration, login, and authentication.
- `templates/` – Shared templates and app-specific UI components.
- `static/` – CSS, JS, images, etc.

## ⚙️ Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/wayfair-clone.git
cd wayfair-clone

```
### 2. Set Up a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

> If `requirements.txt` doesn’t exist yet, run:
```bash
pip freeze > requirements.txt
```

### 4. Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create a Superuser (Optional)

```bash
python manage.py createsuperuser
```

### 6. Run the Development Server

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` to see the app in action!

## 🛠️ To Do (Coming Soon)

- Add to Cart / Checkout functionality  
- Product Reviews  
- User Profiles (My Account & My Orders pages)  
- Admin dashboard improvements  
- Mobile navigation polish

---

## 📌 Notes

This project is still under active development and not intended for production use.  
Feel free to fork, clone, or contribute!

```
