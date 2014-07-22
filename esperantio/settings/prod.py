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
