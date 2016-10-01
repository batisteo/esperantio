from .models import Arangxo, Evento
from rest_framework import serializers


class EventoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Evento
        fields = ('komenco', 'fino', 'temo', 'arangxo', 'lat', 'long')


class ArangxoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Arangxo
        fields = ('nomo', 'mallonga_nomo', 'slug', 'eventoj')
