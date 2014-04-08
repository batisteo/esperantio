from django.utils.translation import ugettext_lazy as _
from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth import authenticate

from .models import Uzanto


class UzantoCreateForm(forms.ModelForm):
    error_messages = {
        'duplicate_username': _("A user with that username already exists."),
        'password_mismatch': _("The two password fields didn't match."),
    }
    salutnomo = forms.RegexField(label=_("Username"), max_length=30,
        regex=r'^[\w.@+-]+$',
        help_text=_("Required. 30 characters or fewer. Letters, digits and "
                      "@/./+/-/_ only."),
        error_messages={
            'invalid': _("This value may contain only letters, numbers and "
                     "@/./+/-/_ characters.")})
    pasvorto1 = forms.CharField(label=_("Password"),
        widget=forms.PasswordInput)
    pasvorto2 = forms.CharField(label=_("Password confirmation"),
        widget=forms.PasswordInput,
    help_text=_("Enter the same password as above, for verification."))

    def clean_salutnomo(self):
        salutnomo = self.cleaned_data["salutnomo"]
        try:
            Uzanto._default_manager.get(salutnomo=salutnomo)
        except Uzanto.DoesNotExist:
            return salutnomo
        raise forms.ValidationError(
            self.error_messages['duplicate_username'],
            code='duplicate_username',
        )

    def clean_password2(self):
        pasvorto1 = self.cleaned_data.get("pasvorto1")
        pasvorto2 = self.cleaned_data.get("pasvorto2")
        if pasvorto1 and pasvorto2 and pasvorto1 != pasvorto2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )
        return pasvorto2

    class Meta:
        model = Uzanto
        fields = [
                'salutnomo',
                'pasvorto1',
                'pasvorto2',
                'retposxto',
        ]
    
    def save(self, commit=True):
        uzanto = super(UzantoCreateForm, self).save(commit=False)
        pasvorto = self.cleaned_data['pasvorto1']
        if commit:
            uzanto = Uzanto.objects.create_user(
                    self.cleaned_data['salutnomo'],
                    self.cleaned_data['retposxto'],
                    password=pasvorto,
                    )
            u = authenticate(salutnomo=uzanto.salutnomo, password=pasvorto)
            uzanto.backend = u.backend
            uzanto.save()
        return uzanto


class CustomUserChangeForm(UserChangeForm):
    def __init__(self, *args, **kwargs):
        super(CustomUserChangeForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Uzanto
        fields = [
                "salutnomo",
                "retposxto",
                "persona_nomo",
                "familia_nomo",
                "jabber",
                "skype",
                "twitter",
                "retejo",
                "adreso",
                "adreso2",
                "posxtkodo",
                "urbo",
                "lando",
                "tel",
                "tel2",
        ]
