from .base import *
import config_prod as c

DEBUG = False

TEMPLATE_DEBUG = DEBUG

MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), "public", "media")
STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), "public", "static")

SECRET_KEY = c.SECRET_KEY

ALLOWED_HOSTS = [c.ALLOWED_HOSTS,]

DATABASES = {
    'default': {
        'ENGINE': c.DATABASE_ENGINE,
        'NAME': c.DATABASE_NAME,
        'USER': c.DATABASE_USER,
        'PASSWORD': c.DATABASE_PASSWORD,
        'HOST': c.DATABASE_HOST,
        'PORT': c.DATABASE_PORT,
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'


EMAIL_HOST = c.EMAIL_HOST
EMAIL_PORT = c.EMAIL_PORT
EMAIL_HOST_USER = c.EMAIL_HOST_USER
EMAIL_HOST_PASSWORD = c.EMAIL_HOST_PASSWORD
EMAIL_USE_TLS = c.EMAIL_USE_TLS

