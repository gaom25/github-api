from .common import *  # noqa

from os import environ

ALLOWED_HOSTS = ['*']

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': environ.get('DATABASE_NAME', 'mydatabase'),
        'USER': environ.get('DATABASE_USER', 'mydatabaseuser'),
        'PASSWORD': environ.get('DATABASE_PASSWORD', 'mypassword'),
        'HOST': environ.get('DATABASE_HOST', '127.0.0.1'),
        'PORT': environ.get('DATABASE_PORT', '5432'),
    }
}

INSTALLED_APPS = DEFAULT_APPS + THIRD_PARTY_APPS + LOCAL_APPS  # noqa
