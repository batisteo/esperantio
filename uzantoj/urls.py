from django.conf.urls import patterns, include, url

urlpatterns = patterns('uzantoj.views',
    url(r'^$',
            view='uzanto_detail',
            name='uzanto_detail',),

    url(r'^redakti/$',
            view='uzanto_update',
            name='uzanto_update',),

)
