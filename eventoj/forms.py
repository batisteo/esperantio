from django import forms

from toolbox.forms import MultiForm

from . import models as m

class ArangxoForm(forms.ModelForm):
    class Meta:
        model = m.Arangxo
        fields = (
            "organizo",
            "nomo",
            "longa_nomo",
            "publiko",
            "nb_partoprenantoj",
            "retejo",
            "retposxto",
            "etikedoj",
          )
        widgets = {
            'nomo': forms.TextInput(attrs={'required':''}),
        }


class EventoForm(forms.ModelForm):
    class Meta:
        model = m.Evento
        fields = (
            "komenco",
            "fino",
            "urbo",
            "posxtkodo",
            "lando",
            "priskribo",
            "nb_partoprenantoj",
            "lat",
            "long",
        )
        widgets = {
            "nb_partoprenantoj": forms.HiddenInput(),
            "komenco": forms.HiddenInput(),
            "fino": forms.HiddenInput(),
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


class EventoArangxoCreateForm(MultiForm):
    forms = [
        ('arangxo', ArangxoForm),
        ('evento', EventoForm),
    ]
    
    def save(self):
        forms = dict(self.forms)
        arangxo = forms['arangxo'].save()
        print arangxo, arangxo.pk
        evento = forms['evento'].save(commit=False)
        evento.arangxo = arangxo
        print evento.arangxo
        evento.save()
        print evento, evento.pk
        return evento
