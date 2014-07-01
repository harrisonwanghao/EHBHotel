#coding: utf-8
"""
Django settings for ehbhotel project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)

import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '&pksv5vpicf+&yo6(9u!ghage$9oo=a4#4^ld625xb+e@%k)^q'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'customers',
    'rooms',
    'reservations',
    'dinner',
    'products',
    'transactions',
    'statistics',
    'employee',
    'kiosk',
    'chart_tools',
    'ganalytics',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

TEMPLATE_DIRS = (
    BASE_DIR + '/templates/'
)

ROOT_URLCONF = 'ehbhotel.urls'

WSGI_APPLICATION = 'ehbhotel.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'nl-be'

TIME_ZONE = 'Europe/Brussels'

DATE_INPUT_FORMATS = ('%d/%m/%Y','%Y/%m/%d')

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static/'),
)

# Email
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'musilitar@gmail.com'
EMAIL_HOST_PASSWORD = '33lolbrol33'

# Analytics

GANALYTICS_TRACKING_CODE = 'UA-51195444-1'

AUTHENTICATION_BACKENDS = (
    'django_auth_ldap.backend.ActiveDirectoryAuthentication',
    'django.contrib.auth.backends.ModelBackend'
)
AUTH_USER_MODEL = 'customers.Customer'
