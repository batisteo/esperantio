from .base import *
from . import hidden

DEBUG = True

SECRET_KEY = 'N0_s3kr*t_k3y'

INSTALLED_APPS += (
    'debug_toolbar.apps.DebugToolbarConfig',
)
