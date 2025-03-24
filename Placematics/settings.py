from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Security settings
SECRET_KEY = 'your-secret-key-here-replace-this-with-a-long-random-string'  # Replace with a secure key
DEBUG = True  # Set to False in production
ALLOWED_HOSTS = []  # Add your domain/IP in production, e.g., ['localhost', 'yourdomain.com']

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',       # Admin interface
    'django.contrib.auth',        # Authentication system (default User model)
    'django.contrib.contenttypes',# Framework for content types
    'django.contrib.sessions',    # Session management
    'django.contrib.messages',    # Messaging framework
    'django.contrib.staticfiles', # Static file handling
    'placements',                 # Your custom app
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Placematics.urls'

WSGI_APPLICATION = 'Placematics.wsgi.application'  # Fixed: Correct path to wsgi.py

# Database (using SQLite for development)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'  # Change to your timezone, e.g., 'Asia/Kolkata' for India
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'placements' / 'static']  # Custom static files
STATIC_ROOT = BASE_DIR / 'staticfiles'  # For production (collectstatic)

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Login/Logout redirects (optional, adjust as needed)
LOGIN_URL = '/'
LOGOUT_REDIRECT_URL = '/'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'Placematics' / 'templates'],  # Project-level templates
        'APP_DIRS': True,  # Enable app-level templates (e.g., placements/templates/)
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]