# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS


BASE_DIR = os.path.dirname(os.path.dirname(__file__))


TEMPLATE_DIRS = (os.path.join(BASE_DIR, 'templates'), )

MEDIA_URL = '/media/'
STATIC_URL = '/static/'

STATICFILES_DIRS = (os.path.join(BASE_DIR, "static"), )


AUTH_USER_MODEL = 'uzantoj.Uzanto'
LOGIN_URL = '/uzanto/konekti/'
LOGIN_REDIRECT_URL = '/uzanto/'


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'uzantoj',
    'eventoj',
    'organizoj',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS += (
    'django.core.context_processors.request',
)

ROOT_URLCONF = 'esperantio.urls'

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'eo'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

