# Django Project with Login & Registration

A Django web application with user authentication (login/registration) and MySQL database.

## Features

- 🏠 Landing page
- 🔐 User registration
- 🔑 User login/logout
- 🗄️ MySQL database integration
- 🎨 Modern responsive UI

## Setup Instructions

### 1. Prerequisites

- Python 3.8 or higher
- MySQL Server installed and running

### 2. Create MySQL Database

Open MySQL and create a database:

```sql
CREATE DATABASE myproject_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

### 3. Install Dependencies

Create a virtual environment and install dependencies:

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 4. Configure Database

Edit `myproject/settings.py` and update the database settings with your MySQL credentials:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'myproject_db',
        'USER': 'root',  # Your MySQL username
        'PASSWORD': 'your_password',  # Your MySQL password
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

### 5. Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Create Superuser (Optional)

```bash
python manage.py createsuperuser
```

### 7. Run the Development Server

```bash
python manage.py runserver
```

Visit http://127.0.0.1:8000/ in your browser.

## Project Structure

```
revadjango/
├── myproject/              # Main project directory
│   ├── settings.py         # Project settings (database config)
│   ├── urls.py             # Main URL configuration
│   ├── wsgi.py
│   └── asgi.py
├── accounts/               # Accounts app
│   ├── views.py            # Login, register, landing views
│   ├── urls.py             # App URL patterns
│   ├── models.py
│   └── apps.py
├── templates/              # HTML templates
│   ├── base.html           # Base template
│   └── accounts/
│       ├── landing.html    # Landing page
│       ├── login.html      # Login page
│       └── register.html   # Registration page
├── manage.py               # Django management script
└── requirements.txt        # Python dependencies
```

## Available Pages

- **Home/Landing**: http://127.0.0.1:8000/
- **Register**: http://127.0.0.1:8000/register/
- **Login**: http://127.0.0.1:8000/login/
- **Admin**: http://127.0.0.1:8000/admin/

## Technologies Used

- Django 4.2
- MySQL Database
- HTML/CSS (with embedded styles)
- Django Authentication System

## Notes

- Remember to keep `SECRET_KEY` secure in production
- Set `DEBUG = False` in production
- Update `ALLOWED_HOSTS` for production deployment
- The templates include modern, responsive CSS styling
