from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    url(r'^konekti/$',
        view='django.contrib.auth.views.login',
        name='konekti'),

    url(r'^elsaluti/$',
        view='django.contrib.auth.views.logout', kwargs={'next_page': '/'},
        name='elsaluti'),
)


urlpatterns += patterns('uzantoj.views',
    url(r'^$',
            view='uzanto_detail',
            name='uzanto_detail',),

    url(r'^redakti/$',
            view='uzanto_update',
            name='uzanto_update',),
)
