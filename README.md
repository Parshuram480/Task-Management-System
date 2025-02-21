# Task Management System

This is a Django-based Task Management System that allows users to manage their tasks efficiently. The project uses PostgreSQL as the database and Bootstrap for frontend styling.

## Features
- User authentication (Login/Register/Logout)
- Create, update, delete, and toggle task status
- Responsive design using Bootstrap
- PostgreSQL database integration

## Installation and Setup

### 1. Clone the Repository
```sh
git clone https://github.com/Parshuram480/Task-Management-System.git
cd Task-Management-System
```

### 2. Create and Activate Virtual Environment
```sh
python -m venv venv
# Activate the virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 3. Install Dependencies
```sh
pip install -r requirements.txt
```

### 4. Create Database in PostgreSQL
Manually create a database in PostgreSQL:
- **Database Name**: `task_management`

### 5. Configure Database in Django
Edit the `DATABASES` setting in `settings.py`:
```python
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "task_management",  # Change database name if needed
        "USER": "postgres",          # Change user if needed
        "PASSWORD": "1238",         # Change password
        "HOST": "127.0.0.1",        # Change host address if needed
        "PORT": "5432",             # Change port if needed
    }
}
```

### 6. Apply Migrations
```sh
cd task_management_system
python manage.py makemigrations
python manage.py migrate
```

### 7. Run the Development Server
```sh
python manage.py runserver
```
Then open your browser and go to `http://127.0.0.1:8000/`.

## License
This project is open-source and available under the [MIT License](LICENSE).

## Author
[Parshuram480](https://github.com/Parshuram480)
