from .base import *

DEBUG = True

SECRET_KEY = 'N0_s3kr*t_k3y'

INSTALLED_APPS += (
    'debug_toolbar.apps.DebugToolbarConfig',
)

# MailDump https://github.com/ThiefMaster/maildump http://mailcatcher.me/
EMAIL_HOST = '127.0.0.1'
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_PORT = 1025
EMAIL_USE_TLS = False
