import sys
from os import environ
from os.path import abspath, basename, dirname, join, normpath

DJANGO_ROOT = dirname(dirname(abspath(__file__)))

PROJECT_ROOT = dirname(DJANGO_ROOT)

SECRET_KEY = environ.get(
    'SECRET_KEY',
    'abcdefghijklmnopqrstuvwxyz0123456789!$%&()=+-_'
)

SITE_NAME = basename(DJANGO_ROOT)

STATIC_ROOT = join(PROJECT_ROOT, 'run', 'static')

MEDIA_ROOT = join(PROJECT_ROOT, 'run', 'images')

STATICFILES_DIRS = [
    join(PROJECT_ROOT, 'static'),
]

PROJECT_TEMPLATES = [
    join(PROJECT_ROOT, 'templates'),
]

sys.path.append(normpath(join(PROJECT_ROOT, 'apps')))

DEFAULT_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

THIRD_PARTY_APPS = [
    'rest_framework',
]

LOCAL_APPS = [
    'stats'
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

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': PROJECT_TEMPLATES,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages'
            ],
        },
    },
]

SECRET_FILE = normpath(join(PROJECT_ROOT, 'run', 'SECRET.key'))

ADMINS = (
    (
        environ.get(
            'ADMINS_NAME',
            'name'
        ),
        environ.get(
            'ADMINS_EMAIL',
            'email@admins.net'
        )
    ),
)

MANAGERS = ADMINS

ROOT_URLCONF = f'{SITE_NAME}.urls'

SITE_ID = 1

STATIC_URL = '/static/'

MEDIA_URL = '/images/'

DEBUG = False

LANGUAGE_CODE = 'en-US'

TIME_ZONE = environ.get(
    'TIME_ZONE',
    'America/Bogota'
)

USE_I18N = True

USE_L10N = True

USE_TZ = True

LOGGING = {
    'version': 1,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s :: %(asctime)s :: '
                      '%(name)s :: %(process)d %(thread)d :: %(message)s'
        }
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': environ.get('LOG_LEVEL', 'INFO')
        },
        'stats': {
            'handlers': ['console'],
            'level': environ.get('LOG_LEVEL', 'INFO')
        }
    }
}

REST_FRAMEWORK = {
    'EXCEPTION_HANDLER': 'utils.handlers.exception_errors_format_handler',
}

TOKEN_DURATION = int(environ.get('TOKEN_DURATION', 10000))
