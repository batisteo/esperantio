from django.conf.urls import url

from organizoj.views import organizo_list, organizo_create, organizo_detail, organizo_update

urlpatterns = [
    url(r'^$',
        view=organizo_list,
        name='organizo_list',),

    url(r'^aldoni/$',
        view=organizo_create,
        name='organizo_create',),

    url(r'^(?P<pk>\d+)/$',
        view=organizo_detail,
        name='organizo_detail',),

    url(r'^(?P<pk>\d+)/redakti/$',
        view=organizo_update,
        name='organizo_update',),
]
