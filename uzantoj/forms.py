from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import Uzanto


class CustomUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Uzanto


class CustomUserChangeForm(UserChangeForm):
    def __init__(self, *args, **kwargs):
        super(CustomUserChangeForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Uzanto


class UzantoCreateForm(forms.ModelForm):
    class Meta:
        model = Uzanto
        fields = [
                'salutnomo',
                'password',
                'retposxto',
        ]
