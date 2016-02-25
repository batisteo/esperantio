from django.contrib import admin

from markitup.widgets import AdminMarkItUpWidget

from .models import Arangxo, Evento


@admin.register(Arangxo)
class ArangxoAdmin(admin.ModelAdmin):
    list_display = ('mallonga_nomo', 'nomo', 'slug', 'publiko', 'min_homoj', 'max_homoj', 'ofteco', 'dauro')


@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'temo', 'komenco', 'fino', 'urbo', 'lando', 'kreanto')

    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name == 'content':
            kwargs['widget'] = AdminMarkItUpWidget()
        return super(EventoAdmin, self).formfield_for_dbfield(db_field, **kwargs)



