from .base import *
from . import hidden


SECRET_KEY = hidden.SECRET_KEY

ALLOWED_HOSTS = ["esperant.io"]

SERVER_EMAIL = hidden.EMAIL['SERVER_EMAIL']
EMAIL_HOST = hidden.EMAIL['HOST']
EMAIL_PORT = hidden.EMAIL['PORT']
EMAIL_USE_TLS = hidden.EMAIL['USE_TLS']
EMAIL_USE_SSL = hidden.EMAIL['USE_SSL']
EMAIL_HOST_USER = hidden.EMAIL['HOST_USER']
EMAIL_HOST_PASSWORD = hidden.EMAIL['HOST_PASSWORD']
