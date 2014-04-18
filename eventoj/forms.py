from datetime import date, datetime

from django.utils.translation import ugettext_lazy as _
from django import forms
from django.forms.widgets import HiddenInput, Textarea

from django_countries import countries
from taggit.forms import TagField
from . import models as m
from .elektoj import PUBLIKO_ELEKTOJ

class RenkontigxoForm(forms.Form):
    nomo = forms.CharField(widget=forms.TextInput(attrs={'required': ''}),
            label=_("nomo"))
    mallonga_nomo = forms.CharField(required=False,
            label=_("mallonga nomo"))
    publiko = forms.ChoiceField(required=False,
            label=_("publiko"), choices=PUBLIKO_ELEKTOJ)
    retejo = forms.URLField(required=False,
            widget=forms.URLInput(attrs={'placeholder': 'http://'}),
            label=_("retejo"))
    nb_partoprenantoj = forms.IntegerField(
            widget=forms.NumberInput(attrs={
                'required': '',
                'pattern': '[1-9]{4}',
                'maxlength': '4'}),
            label=_("nombro da partoprenantoj"),
            help_text=_("Averagxa aux estimata nombro da partoprenantoj."))

    etikedoj = TagField(required=False,
            label=_("etikedoj"))
    temo = forms.CharField(required=False,
            label=_("temo"))
    urbo = forms.CharField(widget=forms.TextInput(attrs={'required': ''}),
            label=_("urbo"))
    posxtkodo = forms.CharField(required=False,
            label=_("posxtkodo"))
    lando = forms.ChoiceField(widget=forms.Select(attrs={'required': ''}),
            choices=countries,
            label=_("lando"))
    priskribo = forms.CharField(required=False, widget=Textarea,
            label=_("priskribo"))
    komenco = forms.DateTimeField( widget=HiddenInput,
            label=_("komenco"))
    fino = forms.DateTimeField(required=False, widget=HiddenInput,
            label=_("fino"))
    lat = forms.FloatField( widget=HiddenInput,
            label=_("lat"))
    long = forms.FloatField( widget=HiddenInput,
            label=_("long"))


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

