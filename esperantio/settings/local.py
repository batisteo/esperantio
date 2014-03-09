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
        'ENGINE': c.DATABASE_ENGINE,
        'NAME': c.DATABASE_NAME,
    }
}
