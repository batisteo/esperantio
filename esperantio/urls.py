from django.conf.urls import patterns, include, url

from evento.views import HybridDetailView
from evento.models import Evento

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'esperantio.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)


urlpatterns += patterns('evento.views',
    url(r'^kal/arangxo/$',
            view='arangxo_list',
            name='arangxo_list',),

    url(r'^kal/arangxo/aldoni/$',
            view='arangxo_create',
            name='arangxo_create',),

    url(r'^kal/arangxo/(?P<pk>\d+)/$',
            view='arangxo_detail',
            name='arangxo_detail',),

    url(r'^kal/arangxo/(?P<pk>\d+)/redakti/$',
            view='arangxo_update',
            name='arangxo_update',),

    url(r'^kal/evento/$',
            view='evento_list',
            name='evento_list',),

    url(r'^kal/arangxo/(?P<pk>\d+)/evento/aldoni/$',
            view='evento_create',
            name='evento_create',),

    url(r'^kal/evento/(?P<pk>\d+)/$',
            view=HybridDetailView.as_view(model=Evento),
            name='evento_detail',),

    url(r'^kal/evento/(?P<pk>\d+)/$',
            view='evento_detail',
            name='evento_detail',),

    url(r'^kal/evento/(?P<pk>\d+)/redakti/$',
            view='evento_update',
            name='evento_update',),

)
