from django import forms

from toolbox.forms import MultiForm

from . import models as m

class ArangxoForm(forms.ModelForm):
    class Meta:
        model = m.Arangxo
        fields = (
            "organizo",
            "nomo",
            "mallonga_nomo",
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
            "temo",
            "urbo",
            "posxtkodo",
            "lando",
            "priskribo",
            "nb_partoprenantoj",
            "komenco",
            "fino",
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

    def save(self, commit=True):
        evento = super(EventoCreateForm, self).save(commit=False)
        evento.arangxo = self.arangxo
        evento.kreanto = self.kreanto
        if commit:
            evento.save()
        return evento


class EventoArangxoCreateForm(MultiForm):
    forms = [
        ('arangxo', ArangxoForm),
        ('evento', EventoForm),
    ]
    
    def __init__(self, *args, **kwargs):
        self.kreanto = kwargs.pop('kreanto')
        super(EventoArangxoCreateForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        forms = dict(self.forms)
        arangxo = forms['arangxo'].save(commit=False)
        arangxo.kreanto = self.kreanto
        if commit:
            arangxo.save()
        evento = forms['evento'].save(commit=False)
        evento.arangxo = arangxo
        evento.kreanto = self.kreanto
        if commit:
            evento.save()
        return evento
