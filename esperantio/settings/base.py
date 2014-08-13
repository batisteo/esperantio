# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS


BASE_DIR = os.path.dirname(os.path.dirname(__file__))

SITE_ID = 1
TEMPLATE_DIRS = (os.path.join(BASE_DIR, 'templates'), )

MEDIA_URL = '/media/'
STATIC_URL = '/static/'

STATICFILES_DIRS = (os.path.join(BASE_DIR, "static"), )


AUTH_USER_MODEL = 'uzantoj.Uzanto'
LOGIN_URL = '/uzanto/konekti/'
LOGIN_REDIRECT_URL = '/'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

ADMINS = (
    ('Baptiste Darthenay', 'bonvenon@esperant.io'),
)

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.flatpages',
    'django_extensions',
    'django_gravatar',
    'django_countries',
    'flatpages_x',
    'markitup',
    'markdown_deux',
    'braces',
    'taggit',
    'leaflet',
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
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware'
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

LEAFLET_CONFIG = {
    'DEFAULT_CENTER': (45.1, 3.9),
    'DEFAULT_ZOOM': 4,
    'MIN_ZOOM': 3,
    'MAX_ZOOM': 16,
    'TILES': 'http://{s}.tile.openstreetmap.fr/hot/{z}/{x}/{y}.png',
    # 'TILES': 'http://api.tiles.mapbox.com/v3/batisteo.hknl8e1c/{z}/{x}/{y}.png',
    'ATTRIBUTION_PREFIX': 'Mapaj datumoj &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> kontribuantoj',
    'RESET_VIEW': False,
}

GRAVATAR_SECURE = True
GRAVATAR_DEFAULT_IMAGE = "mm"

MARKITUP_SET = 'markitup/sets/markdown'
MARKITUP_SKIN = 'markitup/skins/simple'
MARKITUP_FILTER = ('markdown2.markdown', {'safe_mode': True})
