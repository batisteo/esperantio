from django import forms
from . import models as m


class ArangxoForm(forms.ModelForm):
    class Meta:
        model = m.Arangxo
        fields = (
            "nomo",
            "longa_nomo",
            "organizo",
            "etikedoj",
            "publiko",
            "nb_partoprenantoj",
          )


class EventoForm(forms.ModelForm):
    class Meta:
        model = m.Evento
        fields = (
            "lat",
            "long",
            "komenco",
            "fino",
            "retejo",
            "retposxto",
            "urbo",
            "posxtkodo",
            "lando",
            "nb_partoprenantoj",
        )
        widgets = {
            "lat": forms.HiddenInput(),
            "long": forms.HiddenInput(),
        }


class EventoCreateForm(EventoForm):
    def __init__(self, *args, **kwargs):
        self.arangxo = m.Arangxo.objects.get(pk=kwargs.pop('arangxo'))
        super(EventoForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        evento = super(EventoForm, self).save(commit=False)
        evento.arangxo = self.arangxo
        if commit:
            evento.save()
        return evento
