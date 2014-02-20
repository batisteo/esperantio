from .base import *

DEBUG = True

TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = [get_env_variable("ALLOWED_HOSTS"),]

DATABASES = {
    'default': {
        'ENGINE': get_env_variable("DATABASE_ENGINE"),
        'NAME': get_env_variable("DATABASE_NAME"),
        'USER': get_env_variable("DATABASE_USER"),
        'PASSWORD': get_env_variable("DATABASE_PASSWORD"),
        'HOST': get_env_variable("DATABASE_HOST"),
        'PORT': get_env_variable("DATABASE_PORT"),
    }
}
