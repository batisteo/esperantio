from django.conf.urls import patterns, include, url

urlpatterns = patterns('eventoj.views',
    url(r'^arangxo/$',
            view='arangxo_list',
            name='arangxo_list',),

    url(r'^arangxo/aldoni/$',
            view='arangxo_create',
            name='arangxo_create',),

    url(r'^(?P<slug>[\w-]+)/redakti/$',
            view='arangxo_update',
            name='arangxo_update',),

    url(r'^evento/aldoni/$',
            view='evento_arangxo_create',
            name='evento_arangxo_create',),

    url(r'^(?P<slug>[\w-]+)/evento/aldoni/$',
            view='evento_create',
            name='evento_create',),

    url(r'^(?P<slug>[\w-]+)/(?P<jaro>\d{4})(?:/(?P<monato>\d+))?(?:/(?P<tago>\d+))?/$',
            view='evento_detail',
            name='evento_detail',),

    url(r'^(?P<slug>[\w-]+)/(?P<jaro>\d{4})(?:/(?P<monato>\d+))?(?:/(?P<tago>\d+))?/redakti/$',
            view='evento_update',
            name='evento_update',),

    url(r'^evento/json/$',
            view='evento_json_list',
            name='evento_json_list',),

    url(r'^(?P<slug>[\w-]+)/$',
            view='arangxo_detail',
            name='arangxo_detail',),
)
