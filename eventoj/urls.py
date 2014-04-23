from django.conf.urls import patterns, include, url

urlpatterns = patterns('eventoj.views',
    url(r'^arangxo/$',
            view='arangxo_list',
            name='arangxo_list',),

    url(r'^arangxo/aldoni/$',
            view='arangxo_create',
            name='arangxo_create',),

    url(r'^arangxo/(?P<pk>\d+)/$',
            view='arangxo_detail',
            name='arangxo_detail',),

    url(r'^arangxo/(?P<pk>\d+)/redakti/$',
            view='arangxo_update',
            name='arangxo_update',),

    url(r'^evento/$',
            view='evento_list',
            name='evento_list',),

    url(r'^evento/aldoni/$',
            view='evento_arangxo_create',
            name='evento_arangxo_create',),

    url(r'^arangxo/(?P<pk>\d+)/evento/aldoni/$',
            view='evento_create',
            name='evento_create',),

    url(r'^evento/(?P<pk>\d+)/$',
            view='evento_detail',
            name='evento_detail',),

    url(r'^evento/(?P<pk>\d+)/redakti/$',
            view='evento_update',
            name='evento_update',),

)
