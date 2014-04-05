from django.conf.urls import patterns, include, url
from django.contrib import admin
from django_markdown import flatpages

admin.autodiscover()
flatpages.register()

urlpatterns = patterns('',
    url(r'^', include('eventoj.urls')),
    
    url(r'^admin/', include(admin.site.urls)),
    url(r'^uzanto/', include('uzantoj.urls')),
    url(r'^organizo/', include('organizoj.urls')),
    url('^markdown/', include( 'django_markdown.urls')),
)

urlpatterns += patterns('django.contrib.flatpages.views',
    url(r'^helpo/$', 'flatpage', {'url': '/helpo/'}, name='helpo'),
    url(r'^kontribui/$', 'flatpage', {'url': '/kontribui/'}, name='kontribui'),
    url(r'^api/$', 'flatpage', {'url': '/api/'}, name='api'),
    url(r'^kontakto/$', 'flatpage', {'url': '/kontakto/'}, name='kontakto'),
    url(r'^pri-ni/$', 'flatpage', {'url': '/pri-ni/'}, name='pri-ni'),
)
