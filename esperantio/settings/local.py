from .base import *
import config_local as c

DEBUG = True

TEMPLATE_DEBUG = DEBUG

SECRET_KEY = c.SECRET_KEY

INSTALLED_APPS += (
    'debug_toolbar',
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
