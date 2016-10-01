# Build paths inside the project like this: path.join(BASE_DIR, ...)
from os import path


PROJECT_DIR = path.dirname(path.dirname(path.abspath(__file__)))
BASE_DIR = path.dirname(PROJECT_DIR)

SITE_ID = 1

# Static files (CSS, JavaScript, Images)

STATIC_URL = '/static/'
MEDIA_URL = '/media/'

STATICFILES_DIRS = [path.join(PROJECT_DIR, 'static')]
STATIC_ROOT = path.join(BASE_DIR, 'public/static')
MEDIA_ROOT = path.join(BASE_DIR, 'public/media')


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [path.join(PROJECT_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.template.context_processors.i18n',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

AUTH_USER_MODEL = 'uzantoj.Uzanto'
LOGIN_URL = '/uzanto/konekti/'
LOGIN_REDIRECT_URL = '/'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'esperantio',
    }
}

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
    'rest_framework',
    'corsheaders',
    'markitup',
    'markdown_deux',
    'braces',
    'taggit',
    'leaflet',

    'uzantoj',
    'eventoj',
    'organizoj',
)
DEBUG_TOOLBAR_PANELS = (
  'debug_toolbar.panels.version.VersionDebugPanel',
  'debug_toolbar.panels.timer.TimerDebugPanel',
  'debug_toolbar.panels.profiling.ProfilingDebugPanel',
)
MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware'
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
    'TILES': 'https://{s}.tile.openstreetmap.fr/hot/{z}/{x}/{y}.png',
    'ATTRIBUTION_PREFIX': 'Mapaj datumoj &copy; <a href="https://openstreetmap.org">OpenStreetMap</a> kontribuantoj',
    'RESET_VIEW': False,
}

GRAVATAR_SECURE = True
GRAVATAR_DEFAULT_IMAGE = "mm"

MARKITUP_SET = 'markitup/sets/markdown'
MARKITUP_SKIN = 'markitup/skins/simple'
MARKITUP_FILTER = ('markdown2.markdown', {'safe_mode': True})

REST_FRAMEWORK = {
    # 'DEFAULT_PERMISSION_CLASSES': ('rest_framework.permissions.IsAdminUser',),
    # 'PAGE_SIZE': 10,
    'EXCEPTION_HANDLER': 'rest_framework_json_api.exceptions.exception_handler',
    'DEFAULT_PAGINATION_CLASS':
        'rest_framework_json_api.pagination.PageNumberPagination',
    'DEFAULT_PARSER_CLASSES': (
        'rest_framework_json_api.parsers.JSONParser',
        'rest_framework_xml.parsers.XMLParser',
        'rest_framework.parsers.FormParser',
        'rest_framework.parsers.MultiPartParser'
    ),
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework_json_api.renderers.JSONRenderer',
        'rest_framework_xml.renderers.XMLRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ),
    'DEFAULT_METADATA_CLASS': 'rest_framework_json_api.metadata.JSONAPIMetadata',
}

CORS_ORIGIN_ALLOW_ALL = True
# CORS_URLS_REGEX = r'^/api.*$'
