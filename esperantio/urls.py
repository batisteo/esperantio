from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'esperantio.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)


urlpatterns += patterns('evento.views',
    url(r'^evento/$',
            view='evento_list',
            name='evento_list',),

    url(r'^evento/aldoni/$',
            view='evento_create',
            name='evento_create',),

    url(r'^evento/(?P<pk>\d+)/$',
            view='evento_detail',
            name='evento_detail',),

    url(r'^evento/(?P<pk>\d+)/redakti/$',
            view='evento_update',
            name='evento_update',),

)
