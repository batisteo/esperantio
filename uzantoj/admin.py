from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ugettext_lazy as _

from .models import Uzanto
from .forms import CustomUserChangeForm, CustomUserCreationForm


class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('salutnomo', 'password')}),
        (_('Personal info'), {'fields': ('persona_nomo', 'familia_nomo')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'aligxdato')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('salutnomo', 'retposxto', 'password1', 'password2')}
        ),
    )
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm
    list_display = ('salutnomo', 'retposxto', 'persona_nomo', 'familia_nomo', 'is_staff')
    search_fields = ('salutnomo', 'retposxto', 'persona_nomo', 'familia_nomo')
    ordering = ('salutnomo',)

admin.site.register(Uzanto, CustomUserAdmin)
