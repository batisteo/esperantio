from datetime import date, datetime

from django.utils.translation import ugettext_lazy as _
from django import forms
from django.forms.widgets import HiddenInput, Textarea

from django_countries import countries
from taggit.forms import TagField
from . import models as m
from .elektoj import PUBLIKO_ELEKTOJ

class RenkontigxoForm(forms.Form):
    nomo = forms.CharField(required=False, label=_("nomo"))
    mallonga_nomo = forms.CharField(required=False, label=_("mallonga_nomo"))
    publiko = forms.ChoiceField(required=False, label=_("publiko"), choices=PUBLIKO_ELEKTOJ)
    retejo = forms.URLField(required=False, label=_("retejo"))
    etikedoj = TagField(required=False, label=_("etikedoj"))
    temo = forms.CharField(required=False, label=_("temo"))
    urbo = forms.CharField(required=False, label=_("urbo"))
    posxtkodo = forms.CharField(required=False, label=_("posxtkodo"))
    lando = forms.ChoiceField(required=False, label=_("lando"), choices=countries)
    priskribo = forms.CharField(required=False, label=_("priskribo"), widget=Textarea)
    nb_partoprenantoj = forms.IntegerField(required=False, label=_("nb_partoprenantoj"))
    komenco = forms.DateTimeField(required=False, label=_("komenco"), widget=HiddenInput)
    fino = forms.DateTimeField(required=False, label=_("fino"), widget=HiddenInput)
    lat = forms.FloatField(required=False, label=_("lat"), widget=HiddenInput)
    long = forms.FloatField(required=False, label=_("long"), widget=HiddenInput)

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

