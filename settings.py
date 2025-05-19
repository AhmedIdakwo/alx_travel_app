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
