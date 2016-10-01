from django.conf.urls import url, include

from rest_framework import routers

from eventoj.views import (
    arangxo_detail, arangxo_list, arangxo_create, arangxo_update,
    cxu_nova_arangxo,
    evento_create, evento_detail, evento_update,
    evento_junulara_list, evento_json_list,
    renkontigxo_nomo_create, renkontigxo_create,
    EventoViewSet, ArangxoViewSet
)

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'eventoj', EventoViewSet)
router.register(r'arangxoj', ArangxoViewSet)

urlpatterns = [
    url(r'^api/', include(router.urls), name='api'),
    url(r'^api/auth/', include('rest_framework.urls', namespace='rest_framework')),

    url(r'^arangxo/$',
        arangxo_list, name='arangxo_list',),

    url(r'^arangxo/aldoni/$',
        arangxo_create, name='arangxo_create',),

    url(r'^eventoj/junularo/$',
        evento_junulara_list, name="junularo",),

    url(r'^(?P<slug>[\w-]+)/redakti/$',
        arangxo_update, name='arangxo_update',),

    url(r'^renkontigxo/aldoni/nomo/$',
        renkontigxo_nomo_create, name='renkontigxo_nomo_create',),

    url(r'^renkontigxo/aldoni/nomo/cxunova/$',
        cxu_nova_arangxo, name='cxu_nova_arangxo',),

    url(r'^renkontigxo/aldoni/$',
        renkontigxo_create, name='renkontigxo_create',),

    url(r'^(?P<slug>[\w-]+)/evento/aldoni/$',
        evento_create, name='evento_create',),

    url(r'^(?P<slug>[\w-]+)/(?P<jaro>\d{4})(?:/(?P<monato>\d+))?(?:/(?P<tago>\d+))?/$',
        evento_detail, name='evento_detail',),

    url(r'^(?P<slug>[\w-]+)/(?P<jaro>\d{4})(?:/(?P<monato>\d+))?(?:/(?P<tago>\d+))?/redakti/$',
        evento_update, name='evento_update',),

    url(r'^evento/json/$',
        evento_json_list, name='evento_json_list',),

    url(r'^(?P<slug>[\w-]+)/$',
        arangxo_detail, name='arangxo_detail',),
]
