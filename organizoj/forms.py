from django import forms
from .models import Organizo

class OrganizoForm(forms.ModelForm):
    class Meta:
        model = Organizo
