from datetime import date, datetime

from django.utils.translation import ugettext_lazy as _
from django import forms
from django.forms.widgets import HiddenInput, Textarea

from django_countries import countries
from taggit.forms import TagField
from . import models as m
from .choices import PublikoElektoj


class RenkontigxoForm(forms.Form):
    nomo = forms.CharField(
            widget=forms.TextInput(attrs={
                'required': '',
                'list': 'nomo_list'}),
            label=_("nomo"))
    mallonga_nomo = forms.CharField(
            widget=forms.TextInput(attrs={'list': 'mallonga_nomo_list'}),
            required=False,
            label=_("mallonga nomo"))
    publiko = forms.ChoiceField(required=False,
            label=_("publiko"), choices=PublikoElektoj.choices)
    retejo = forms.URLField(required=False,
            widget=forms.URLInput(attrs={'placeholder': 'http://'}),
            label=_("retejo"))
    min_homoj = forms.IntegerField(
            widget=forms.NumberInput(attrs={
                'required': '',
                'pattern': '[0-9]{1,4}',
                'maxlength': '4'}),
            label=_("partoprenantoj (min)"))
    max_homoj = forms.IntegerField(
            widget=forms.NumberInput(attrs={
                'required': '',
                'pattern': '[0-9]{1,4}',
                'maxlength': '4'}),
            label=_("partoprenantoj (max)"),
            help_text=_("Averagxa aux estimata nombro da partoprenantoj."))

    etikedoj = TagField(required=False,
            label=_("etikedoj"),
            help_text=_("Ekzemple: prelegoj, ekskursoj, koncertoj"))
    temo = forms.CharField(required=False,
            label=_("temo"))
    urbo = forms.CharField(
            label=_("urbo"))
    posxtkodo = forms.CharField(required=False, widget=HiddenInput,
            label=_("posxtkodo"))
    lando = forms.ChoiceField(widget=forms.Select(attrs={'required': ''}),
            choices=countries,
            label=_("lando"))
    priskribo = forms.CharField(required=False, widget=Textarea,
            label=_("priskribo"))
    komenco = forms.DateTimeField(widget=HiddenInput,
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
            "nomo",
            "mallonga_nomo",
            "publiko",
            "min_homoj",
            "max_homoj",
            "retejo",
            "retposxto",
            "facebook",
            "twitter",
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
            "komenco",
            "fino",
            "lat",
            "long",
        )
        widgets = {
            "komenco": forms.HiddenInput(),
            "fino": forms.HiddenInput(),
            "lat": forms.HiddenInput(),
            "long": forms.HiddenInput(),
        }


class EventoCreateForm(EventoForm):
    def __init__(self, *args, **kwargs):
        arangxo_slug = kwargs.pop('arangxo')
        self.arangxo = m.Arangxo.objects.get(slug=arangxo_slug)
        self.kreanto = self.arangxo.kreanto
        super(EventoCreateForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        evento = super(EventoCreateForm, self).save(commit=False)
        evento.arangxo = self.arangxo
        evento.kreanto = self.kreanto
        if commit:
            evento.save()
        return evento

