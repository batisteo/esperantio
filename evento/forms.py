from django import forms
from . import models as m


class EventoForm(forms.ModelForm):
    class Meta:
        model = m.Evento
        fields = (
            "nomo",
            "lat",
            "long",
            "longa_nomo",
            "komenco",
            "fino",
            "retejo",
            "retposxto",
            "organizo",
            "longa_nomo",
            "urbo",
            "posxtkodo",
            "lando",
            "nb_partopr",
            "skalo",
            "temo",
            "publiko",
        )
        widgets = {
            "lat": forms.HiddenInput(),
            "long": forms.HiddenInput(),
        }
