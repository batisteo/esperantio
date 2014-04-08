from django import forms
from .models import Organizo

class OrganizoForm(forms.ModelForm):
    class Meta:
        model = Organizo
        fields = [
            "nomo",
            "retejo",
            "retposxto",
            "twitter",
            "vera_nomo_bezonata",
            "skalo",
            "adreso",
            "adreso2",
            "posxtkodo",
            "urbo",
            "lando",
            "uzantoj",
        ]
