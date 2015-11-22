command = '/opt/envs/esperantio/bin/gunicorn'
raw_env = ['DJANGO_SETTINGS_MODULE=esperantio.settings.prod']
pythonpath = '/srv/esperantio'
bind = ['127.0.0.1:8010', '[::1]:8010']
workers = 3
user = 'esperantio'
