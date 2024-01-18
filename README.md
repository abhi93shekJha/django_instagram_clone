# Django Instagram Clone ([Explained here](django_notes/dango_basics.md))

### I have written these steps in simple terms to make it easier to understand and follow.

## Overview

Welcome to the Django Instagram Clone project! This project is designed to showcase the following features:

### Server Side Rendering [Explained here](django_notes/django_forms_ServerSideRendering.md)

- Utilizes Django forms created using HTML and CSS.
- Created dummy Instagram signup page.

### Django Rest Framework (DRF) Application [Explained here](django_notes/api_notes.md)

- Implements DRF for enhanced functionality.

### User Authentication [Explained here](django_notes/login_notes.md)

- Provides user registration and login functionalities.
- Utilizes JSON Web Token (JWT) authentication for secure user authentication.

### User Data Management [Explained here](django_notes/follower_model_using_mixin.md)

- Implements CRUD operations for user data using Generics and Mixins.
- Allows users to follow/unfollow others.
- Provides details on followers for a user.
- Retrieves followers and following counts.
- Uses Django ORM for all database interactions.

### Post Management

- Enables CRUD operations for posts.
- Utilizes two tables for posts and multimedia.
- For creating posts, an empty row with `is_published` set to False is initially returned from the post table.
- Multimedia is uploaded separately, and upon posting, the remaining text is added, and `is_published` is set to True.
- [Added Pagination](django_notes/pagination.md)

### Object Level Permissions [Explained here](django_notes/permissions_django.md)

### Asynchronous Tasks with Celery and Redis [Explained here](django_notes/celery_and_redis.md)

- Configured Celery app for running tasks asynchronously.
- Utilizes Redis as a message broker for task queue management.
- Configured Celery Beat for scheduling periodic tasks.



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



