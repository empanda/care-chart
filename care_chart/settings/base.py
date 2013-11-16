"""Base settings shared by all environments"""
# Import global settings to make it easier to extend settings.
from django.conf.global_settings import *   # pylint: disable=W0614,W0401


#==============================================================================
# Directory setup
#==============================================================================

import os
import sys
import care_chart as project_module

PROJECT_DIR = os.path.dirname(os.path.realpath(project_module.__file__))

PROJECT_ROOT = os.path.dirname(PROJECT_DIR)

VAR_ROOT = os.path.join(PROJECT_ROOT, 'var')

BIN_ROOT = os.path.join(PROJECT_ROOT, 'bin')

#==============================================================================
# Generic Django project settings
#==============================================================================

SITE_ID = 1

#==============================================================================
# Admin/managers
#==============================================================================

ADMINS = (
    ('Johann', 'johann+cc@phyfus.com'),
)

MANAGERS = ADMINS

#==============================================================================
# Localization settings
#==============================================================================

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
TIME_ZONE = 'America/Los_Angeles'
USE_TZ = True

USE_I18N = True
USE_L10N = True

LANGUAGE_CODE = 'en'
LANGUAGES = (
    ('en', 'English'),
)

#==============================================================================
# Installed apps
#==============================================================================

INSTALLED_APPS = (
    # Local Apps
    # '{{ project_name }}.apps.',

    # Third Party Apps
    'south',

    # Django Apps
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.admindocs',
)


#==============================================================================
# Project URLS and media settings
#==============================================================================

ROOT_URLCONF = 'care_chart.urls'

LOGIN_URL = '/login/'
LOGOUT_URL = '/logout/'
LOGIN_REDIRECT_URL = '/'

STATIC_URL = '/static/'
MEDIA_URL = '/uploads/'

STATIC_ROOT = os.path.join(VAR_ROOT, 'static')
MEDIA_ROOT = os.path.join(VAR_ROOT, 'uploads')

STATICFILES_DIRS = (
    os.path.join(PROJECT_DIR, 'static'),
)

#==============================================================================
# Templates
#==============================================================================

TEMPLATE_DIRS = (
    os.path.join(PROJECT_DIR, 'templates'),
)

TEMPLATE_CONTEXT_PROCESSORS += (
    'django.core.context_processors.request',
)

#==============================================================================
# Middleware
#==============================================================================

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.transaction.TransactionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

#==============================================================================
# Security settings
#==============================================================================

X_FRAME_OPTIONS = 'DENY'

INTERNAL_IPS = ('127.0.0.1',)

SESSION_COOKIE_HTTPONLY = True

SECURE_CONTENT_TYPE_NOSNIFF = True

SECURE_BROWSER_XSS_FILTER = True

#==============================================================================
# Email settings
#==============================================================================

DEFAULT_FROM_EMAIL = 'webmaster@localhost'

SERVER_EMAIL = DEFAULT_FROM_EMAIL

EMAIL_HOST = 'localhost'

EMAIL_SUBJECT_PREFIX = '[Django - Care Chart] '
