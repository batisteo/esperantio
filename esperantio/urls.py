from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^', include('eventoj.urls')),
    
    url(r'^admin/', include(admin.site.urls)),
    url(r'^uzanto/', include('uzantoj.urls')),
    url(r'^organizo/', include('organizoj.urls')),
)

urlpatterns += patterns('django.contrib.flatpages.views',
    url(r'^helpo/$', 'flatpage', {'url': '/helpo/'}, name='helpo'),
    url(r'^kontribui/$', 'flatpage', {'url': '/kontribui/'}, name='kontribui'),
    url(r'^api/$', 'flatpage', {'url': '/api/'}, name='api'),
    url(r'^kontakto/$', 'flatpage', {'url': '/kontakto/'}, name='kontakto'),
    url(r'^pri-ni/$', 'flatpage', {'url': '/pri-ni/'}, name='pri-ni'),
)
