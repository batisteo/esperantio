from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^uzanto/', include('uzantoj.urls')),

    url(r'^kal/', include('evento.urls')),

    url(r'^ensaluti/$',
        view='django.contrib.auth.views.login',
        name='konekti'),

    url(r'^elsaluti/$',
        view='django.contrib.auth.views.logout',
        name='elsaluti'),
)



