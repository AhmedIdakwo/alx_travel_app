Here’s a detailed step-by-step guide to help you complete your objective of setting up the Django project with all required configurations:

---

### Step 1: Project and App Setup

```bash
# Create project folder and navigate into it
mkdir alx_travel_app && cd alx_travel_app

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install Django and initialize project and app
pip install django
django-admin startproject alx_travel_app .
python manage.py startapp listings
```

---

### Step 2: Install Required Packages

```bash
pip install djangorestframework django-cors-headers drf-yasg celery django-environ mysqlclient
```

If you're using RabbitMQ, ensure it's installed and running locally (`sudo apt install rabbitmq-server`).

---

### Step 3: Update `settings.py`

**In `alx_travel_app/settings.py`:**

```python
import environ
import os

# Initialize environment variables
env = environ.Env()
environ.Env.read_env()

# Add installed apps
INSTALLED_APPS += [
    'rest_framework',
    'corsheaders',
    'listings',
    'drf_yasg',
]

MIDDLEWARE.insert(0, 'corsheaders.middleware.CorsMiddleware')

# CORS settings
CORS_ALLOW_ALL_ORIGINS = True  # or specify allowed origins

# MySQL database settings
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': env('DB_NAME'),
        'USER': env('DB_USER'),
        'PASSWORD': env('DB_PASSWORD'),
        'HOST': env('DB_HOST', default='localhost'),
        'PORT': env('DB_PORT', default='3306'),
    }
}
```

---

### Step 4: Add `.env` File

**Create a `.env` file in the root directory:**

```
DB_NAME=alx_travel
DB_USER=root
DB_PASSWORD=yourpassword
DB_HOST=127.0.0.1
DB_PORT=3306
```

---

### Step 5: Configure Swagger in `urls.py`

**In `alx_travel_app/urls.py`:**

```python
from django.contrib import admin
from django.urls import path, re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="ALX Travel API",
        default_version='v1',
        description="API documentation for travel listings",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
```

---

### Step 6: Initialize Git

```bash
git init
echo "venv/" >> .gitignore
echo ".env" >> .gitignore
git add .
git commit -m "Initial project setup with Swagger, MySQL config, and required dependencies"
```

