from django.conf.urls import patterns, include, url

urlpatterns = patterns('organizoj.views',
    url(r'^$',
            view='organizo_list',
            name='organizo_list',),

    url(r'^aldoni/$',
            view='organizo_create',
            name='organizo_create',),

    url(r'^(?P<pk>\d+)/$',
            view='organizo_detail',
            name='organizo_detail',),

    url(r'^(?P<pk>\d+)/redakti/$',
            view='organizo_update',
            name='organizo_update',),

)
