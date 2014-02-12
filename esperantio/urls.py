from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'esperantio.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^kal/', include('evento.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^ensaluti/$',
        view='django.contrib.auth.views.login',
        name='konekti'),

    url(r'^elsaluti/$',
        view='django.contrib.auth.views.logout',
        name='elsaluti'),
)



