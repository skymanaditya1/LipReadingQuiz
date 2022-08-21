"""
Django settings for lipreading_website project.

Generated by 'django-admin startproject' using Django 3.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
import os
import django_on_heroku

# Build paths inside the project like this: BASE_DIR / 'subdir'.
# All the other paths inside this directory are built as BASE_DIR / 'subdir'
BASE_DIR = Path(__file__).resolve().parent.parent
print(f'This is the base_dir : {BASE_DIR}')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-!vpm2gm0o7mr%83k9zcl9vj&e2_uv#*#r-^f1(x-&i769=dm#('

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    "users",
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'quizzes',
    'questions',
    'results',
    'lipquiz',
    'selection_pages',
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

ROOT_URLCONF = 'lipreading_website.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
                os.path.join(BASE_DIR, 'templates'),
                os.path.join(BASE_DIR, 'quizzes/templates'),
                os.path.join(BASE_DIR, 'users/templates'),
                os.path.join(BASE_DIR, 'lipquiz/templates'),
                os.path.join(BASE_DIR, 'selection_pages/templates'),
            ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.template.context_processors.media',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'lipreading_website.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    # {
    #    'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    # },
    # {
    #    'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    # },
    # {
    #    'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    # },
    # {
    #    'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    # },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/media/'

# This tells Django where the static files are being kept 
# Static directories are defined at the project and application level 
STATICFILES_DIRS = [
    BASE_DIR / "static",
    BASE_DIR / "quizzes" / "static",
    BASE_DIR / "lipquiz" / "static",
    BASE_DIR / "selection_pages" / "static",
]

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# change the login redirect to user dashboard
LOGIN_REDIRECT_URL = "lipquiz:lip-quiz-view"
LOGOUT_REDIRECT_URL = "dashboard"

# SMTP server that django would be using for sending mails to the user
EMAIL_HOST = "localhost"
EMAIL_PORT = 1025

# Activate Django-Heroku
django_on_heroku.settings(locals())