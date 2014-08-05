from django.contrib import admin
from eventoj.models import Arangxo, Evento


@admin.register(Arangxo)
class ArangxoAdmin(admin.ModelAdmin):
    list_display = ('mallonga_nomo', 'nomo', 'slug', 'publiko', 'min_homoj', 'max_homoj', 'ofteco', 'dauro')


@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'temo', 'komenco', 'fino', 'urbo', 'lando', 'kreanto')

