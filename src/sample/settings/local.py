# -*- coding: utf-8 -*-
"""
Django development settings for sample project.
"""
from . import *  # noqa


# Debug
DEBUG = True

TEMPLATES[0]['OPTIONS']['debug'] = DEBUG

ALLOWED_HOSTS = ['*']

# Application definition
INSTALLED_APPS += (
    'debug_toolbar',
)


MIDDLEWARE += (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases
DATABASES = {
    'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'postgres',
            'USER': 'postgres',
            'HOST': 'db',
            'PASSWORD': 'postgres',
            'PORT': 5432,
        }
}


# Debug toolbar
INTERNAL_IPS = ('127.0.0.1',)
