from .base import *
import config_staging as c

DEBUG = True

TEMPLATE_DEBUG = DEBUG

STATIC_ROOT = os.path.join(BASE_DIR, "..", "public", "static")

ALLOWED_HOSTS = [c.ALLOWED_HOSTS),]

DATABASES = {
    'default': {
        'ENGINE': c.DATABASE_ENGINE),
        'NAME': c.DATABASE_NAME),
        'USER': c.DATABASE_USER),
        'PASSWORD': c.DATABASE_PASSWORD),
        'HOST': c.DATABASE_HOST),
        'PORT': c.DATABASE_PORT),
    }
}
