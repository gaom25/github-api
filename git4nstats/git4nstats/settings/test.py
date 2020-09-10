from os import environ
from .common import *  # noqa


DEBUG = True
ROOT_URLCONF = f'{SITE_NAME}.{SITE_NAME}.urls'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': environ.get('TEST_DATABASE_NAME', 'gitlab_ci'),
        'USER': environ.get('TEST_DATABASE_USER', 'postgres'),
        'PASSWORD': environ.get('TEST_DATABASE_PASSWORD', 'admin'),
        'HOST': environ.get('TEST_DATABASE_HOST', 'postgres'),
        'PORT': environ.get('TEST_DATABASE_PORT', '5432'),
    }
}

INSTALLED_APPS = DEFAULT_APPS + THIRD_PARTY_APPS + LOCAL_APPS  # noqa
