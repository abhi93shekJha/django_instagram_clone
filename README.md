# Django Instagram Clone ([Notes link](django_notes/dango_basics.md))

### I have written these steps in simple terms to make it easier to understand and follow.

## Overview

Welcome to the Django Instagram Clone project! This project is designed to showcase the following features:

### Server Side Rendering

- Utilizes Django forms created using HTML and CSS.
- [Notes link](django_notes/django_forms_ServerSideRendering.md)

### Django Rest Framework (DRF) Application

- Implements DRF for enhanced functionality.
- [Notes link](django_notes/api_notes.md)

### User Authentication

- Provides user registration and login functionalities.
- Utilizes JSON Web Token (JWT) authentication for secure user authentication.
- [Notes link](django_notes/login_notes.md)

### User Data Management

- Implements CRUD operations for user data.
- Uses PostgreSQL as the underlying database.


## Setup Instructions

To run the project locally, follow these steps:


### Step 1: Clone the Repository
```bash
git clone https://github.com/abhi93shekJha/django_instagram_clone.git
cd django_instagram_clone
```

### Step 2: Create and Activate Virtual Environment
```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```
    
### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Add 'settings_local.py'
- Copy your settings_local.py file into the 'config' folder.
- File structure is shown below.
```json
DATABASES_LOCAL = {
'default': {
    'ENGINE': 'django.db.backends.postgresql_psycopg2',   # you can use your own database
    'NAME': 'data_base name',      # database name
    'USER': 'user_name',      # user name
    'PASSWORD': 'password',  # password
    'HOST': 'localhost',
    'PORT': '5432',
    }
}
```
### Step 5: Apply Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```
### Step 6: Run the Development Server
```bash
python manage.py runserver
```

Visit http://localhost:8000/ in your browser to view the project.

### Additional Notes
- If you encounter any issues, make sure your virtual environment is activated before running commands.
- Update the database settings in your settings_local.py file as needed.



