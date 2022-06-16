"""
Django settings for kanal_exercise project.

Generated by 'django-admin startproject' using Django 2.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""
import json

import environ
import os

from google.oauth2.service_account import Credentials

env = environ.Env()
# reading .env file
environ.Env.read_env()

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'udb+rg-us-a)u@-d5oit(mogm(7$@+h2ra$@q!j5xoj8j@b$#f'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Django Application
DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

# Inner apps Application
INNER_APPS = ['orders', 'kanal_exercise']

# External Application
EXTERNAL_APPS = [
    'rest_framework',
    'django_crontab'
]

# Application definition
INSTALLED_APPS = DJANGO_APPS + INNER_APPS + EXTERNAL_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'kanal_exercise.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
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

WSGI_APPLICATION = 'kanal_exercise.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DB_NAME', 'kepvicom'),
        'USER': os.getenv('DB_USER', 'crm'),
        'PASSWORD': os.getenv('DB_PASSWORD', 'crm'),
        'HOST': os.getenv('DB_HOST', '127.0.0.1'),
        'PORT': int(os.getenv('DB_PORT', '5433'))
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'

# путь до файла с кредами гугл апи (я использовал сервисный)
# with open(os.path.join(BASE_DIR, os.getenv('GOOGLE_CREDS_PATH', 'path')), 'r') as content:
#     google_creds_json = json.loads(content.read())
# print(google_creds_json)
GOOGLE_CREDS = Credentials.from_service_account_file(os.path.join(BASE_DIR, os.getenv('GOOGLE_CREDS_PATH', 'path')))
# ID файла
GOOGLE_SHEET_ID = os.getenv('SAMPLE_SPREADSHEET_ID', 'file_id')

# Ссылка на список курсов
CB_LINK = 'http://www.cbr.ru/scripts/XML_daily.asp'
# ID доллара
CB_DOLLAR_ID = 'R01235'

# https ссылка для работы  обновления файла через вебхук google drive
GOOGLE_HTTPS_URL_NOTIFY = os.getenv('GOOGLE_HTTPS_URL_NOTIFY', '')

CRONJOBS = [
    ('*/5 * * * *', 'kanal_exercise.cron.my_scheduled_job')
]
