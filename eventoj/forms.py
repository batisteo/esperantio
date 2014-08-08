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
            label=_("nomo de la arangxo"),
            help_text=_("Gxenerala nomo de la arangxo, sen numero nek dato."))
    mallonga_nomo = forms.CharField(
            widget=forms.TextInput(attrs={'list': 'mallonga_nomo_list'}),
            required=False,
            label=_("mallonga nomo"),
            help_text=_("Se tauxgas. Ekzemple: UK, IJK, FESTO, IJS, JES..."))
    kioma = forms.CharField(required=False,
            label=_("kioma evento"))
    temo = forms.CharField(required=False,
            label=_("temo"),
            help_text=_("Ekzemple: 'Genra egaleco', aux nomo de la prelego en klubo."))
    retejo = forms.URLField(required=False,
            widget=forms.URLInput(attrs={'placeholder': 'http://'}),
            label=_("retejo"))

    min_homoj = forms.IntegerField(
            widget=forms.NumberInput(attrs={
                'required': '',
                'pattern': '[0-9]{1,4}',
                'maxlength': '4'}))
    max_homoj = forms.IntegerField(
            widget=forms.NumberInput(attrs={
                'required': '',
                'pattern': '[0-9]{1,4}',
                'maxlength': '4'}),
            help_text=_("Minimuma kaj maksimuma nombro da partoprenantoj atenditaj"))
    publiko = forms.ChoiceField(required=False,
            label=_("publiko"), choices=PublikoElektoj.choices)
    etikedoj = TagField(required=False,
            label=_("etikedoj"),
            help_text=_("Ekzemple: prelegoj, ekskursoj, koncertoj"))
    priskribo = forms.CharField(required=False, widget=Textarea,
            label=_("priskribo"))

    urbo = forms.CharField(
            label=_("urbo"))
    posxtkodo = forms.CharField(required=False, widget=HiddenInput,
            label=_("posxtkodo"))
    lando = forms.ChoiceField(widget=forms.Select(attrs={'required': ''}),
            choices=countries,
            label=_("lando"))
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
            "kioma",
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

