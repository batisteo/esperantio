from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.flatpages.views import flatpage
admin.autodiscover()

urlpatterns = [
    url(r'^helpo/$', flatpage, {'url': '/helpo/'}, name='helpo'),
    url(r'^kontribui/$', flatpage, {'url': '/kontribui/'}, name='kontribui'),
    url(r'^kontakto/$', flatpage, {'url': '/kontakto/'}, name='kontakto'),
    url(r'^pri-ni/$', flatpage, {'url': '/pri-ni/'}, name='pri-ni'),
]


urlpatterns += [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^uzanto/', include('uzantoj.urls')),
    url(r'^organizo/', include('organizoj.urls')),

    url(r'^markitup/', include('markitup.urls')),

    url(r'^$', view='eventoj.views.evento_list', name='hejmo',),

    url(r'^', include('eventoj.urls')),
]
