from datetime import date, datetime

from django import forms
from django.forms.widgets import HiddenInput, Textarea

from django_countries.data import COUNTRIES
from taggit.forms import TagField
from . import models as m
from .elektoj import PUBLIKO_ELEKTOJ

class RenkontigxoForm(forms.Form):
    nomo = forms.CharField()
    mallonga_nomo = forms.CharField()
    publiko = forms.ChoiceField(choices=PUBLIKO_ELEKTOJ)
    retejo = forms.URLField()
    etikedoj = TagField()
    temo = forms.CharField()
    urbo = forms.CharField()
    posxtkodo = forms.CharField()
    lando = forms.ChoiceField(choices=COUNTRIES)
    priskribo = forms.CharField(widget=Textarea)
    nb_partoprenantoj = forms.IntegerField()
    komenco = forms.DateTimeField(widget=HiddenInput)
    fino = forms.DateTimeField(widget=HiddenInput)
    lat = forms.FloatField(widget=HiddenInput)
    long = forms.FloatField(widget=HiddenInput)

    def save(self, user):
        arangxo = m.Arangxo(
                kreanto=user,
                nomo=nomo,
                mallonga_nomo=mallonga_nomo,
                nb_partoprenantoj=nb_partoprenantoj,
                etikedoj=etikedoj,
                publiko=publiko,
        )
        evento = m.Evento(
                arangxo=arangxo,
                komenco=komenco,
                fino=fino,
                lat=lat,
                long=long,
                temo=temo,
                urbo=urbo,
                posxtkodo=posxtkodo,
                lando=lando,
                priskribo=priskribo,
        )
        arangxo.save()
        evento.save()
        print arangxo
        print evento
        return evento

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


class EventoCreateForm(EventoForm):

    def save(self, commit=True):
        evento = super(EventoCreateForm, self).save(commit=False)
        evento.arangxo = self.arangxo
        evento.kreanto = self.kreanto
        if commit:
            evento.save()
        return evento

