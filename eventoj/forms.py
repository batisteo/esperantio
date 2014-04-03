from django import forms

from toolbox.forms import MultiForm

from datetime import date, datetime

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
            "ofteco",
            "dauro",
            "etikedoj",
          )
        widgets = {
            'nomo': forms.TextInput(attrs={'required':''}),
        }

class ArangxoEtaForm(ArangxoForm):
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
            "adreso",
            "adreso2",
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


class EventoEtaForm(EventoForm):
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
        ('arangxo', ArangxoEtaForm),
        ('evento', EventoEtaForm),
    ]
    
    def __init__(self, *args, **kwargs):
        self.kreanto = kwargs.pop('kreanto')
        super(EventoArangxoCreateForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        forms = dict(self.forms)
        nomo = forms['arangxo'].cleaned_data['nomo']
        mallonga_nomo = forms['arangxo'].cleaned_data['mallonga_nomo']
        arangxo1 = m.Arangxo.objects.filter(nomo__iexact=nomo)
        arangxo2 = m.Arangxo.objects.filter(nomo__iexact=mallonga_nomo)
        if arangxo1:
            arangxo = arangxo1[0]
        elif arangxo2:
            arangxo = arangxo2[0]
        else:
            arangxo = forms['arangxo'].save(commit=False)
            arangxo.kreanto = self.kreanto
            fino = forms['evento'].cleaned_data['fino']
            komenco= forms['evento'].cleaned_data['komenco']
            arangxo.dauro = (fino-komenco).days + 1
            if commit:
                arangxo.save()
        evento = forms['evento'].save(commit=False)
        evento.arangxo = arangxo
        evento.kreanto = self.kreanto
        evento.nb_partoprenantoj = arangxo.nb_partoprenantoj
        if commit:
            evento.save()
        return evento
