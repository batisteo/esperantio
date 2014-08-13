from django.conf.urls import patterns, include, url
from django.views.generic import RedirectView
from django.core.urlresolvers import reverse_lazy
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('django.contrib.flatpages.views',
    url(r'^helpo/$', 'flatpage', {'url': '/helpo/'}, name='helpo'),
    url(r'^kontribui/$', 'flatpage', {'url': '/kontribui/'}, name='kontribui'),
    url(r'^api/$', 'flatpage', {'url': '/api/'}, name='api'),
    url(r'^kontakto/$', 'flatpage', {'url': '/kontakto/'}, name='kontakto'),
    url(r'^pri-ni/$', 'flatpage', {'url': '/pri-ni/'}, name='pri-ni'),
)

urlpatterns += patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^uzanto/', include('uzantoj.urls')),
    url(r'^organizo/', include('organizoj.urls')),

    url(r'^markitup/', include('markitup.urls')),
    
    url(r'^$', view='eventoj.views.evento_list', name='hejmo',),
    
    url(r'^', include('eventoj.urls')),
)
