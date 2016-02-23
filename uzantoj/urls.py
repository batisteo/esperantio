from django.conf.urls import url
from django.contrib.auth.views import login, logout

from .views import uzanto_detail, uzanto_update, uzanto_create


urlpatterns = [
    url(r'^konekti/$', view=login, name='konekti'),
    url(r'^elsaluti/$', view=logout, kwargs={'next_page': '/'}, name='elsaluti'),

    url(r'^$', view=uzanto_detail, name='uzanto_detail',),
    url(r'^redakti/$', view=uzanto_update, name='uzanto_update',),
    url(r'^nova/$', view=uzanto_create, name='uzanto_create',),
]
