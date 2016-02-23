from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.db import models
from django.core.mail import send_mail
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone

from django_countries.fields import CountryField


class UzantoManager(BaseUserManager):
    def _create_user(self, salutnomo, retposxto, password,
                     is_active, is_staff, is_superuser, **aliaj_kampoj):
        now = timezone.now()
        if not retposxto:
            raise ValueError(_("Retposxto deviga"))
        retposxto = self.normalize_email(retposxto)
        uzanto = self.model(salutnomo=salutnomo,
                            retposxto=retposxto,
                            last_login=now,
                            aligxdato=now,
                            is_active=is_active,
                            is_staff=is_staff,
                            is_superuser=is_superuser,
                            **aliaj_kampoj)
        uzanto.set_password(password)
        uzanto.save(using=self._db)
        return uzanto

    def create_user(self, salutnomo, retposxto, password=None, **aliaj_kampoj):
        return self._create_user(salutnomo, retposxto, password,
                                 True, False, False, **aliaj_kampoj)

    def create_superuser(self, salutnomo, retposxto, password=None, **aliaj_kampoj):
        return self._create_user(salutnomo, retposxto, password,
                                 True, True, True, **aliaj_kampoj)


class Uzanto(AbstractBaseUser, PermissionsMixin):
    salutnomo = models.CharField(_("salutnomo"), max_length=40, unique=True, db_index=True)
    retposxto = models.EmailField(_("retposxto"), max_length=254, unique=True)
    aligxdato = models.DateTimeField(_("aligxdato"), default=timezone.now)

    persona_nomo = models.CharField(_("persona nomo"), max_length=255)
    familia_nomo = models.CharField(_("familia nomo"), max_length=255)

    jabber = models.EmailField(_("jabber"), max_length=254, blank=True)
    skype = models.CharField(_("skype"), max_length=255, blank=True)
    twitter = models.CharField(_("twitter"), max_length=255, blank=True)
    retejo = models.CharField(_("retejo"), max_length=255, blank=True)

    adreso = models.CharField(_("adreso"), max_length=255, blank=True)
    adreso2 = models.CharField(_("adreso kont."), max_length=255, blank=True)
    posxtkodo = models.CharField(_("posxtkodo"), max_length=10, blank=True)
    urbo = models.CharField(_("urbo"), max_length=255, blank=True)
    lando = CountryField()

    tel = models.CharField(_("telefono"), max_length=20, blank=True)
    tel2 = models.CharField(_("telefono2"), max_length=20, blank=True)

    is_active = models.BooleanField(_("estas aktiva"), default=False)
    is_staff = models.BooleanField(_("estas personaro"), default=False)

    objects = UzantoManager()

    USERNAME_FIELD = 'salutnomo'
    REQUIRED_FIELDS = ['retposxto']

    class Meta:
        verbose_name = _("uzanto")
        verbose_name_plural = _("uzantoj")

    @property
    def nomo(self):
        return self.get_full_name()

    def get_absolute_url(self):
        return "/uzanto/"

    def get_full_name(self):
        return " ".join((self.persona_nomo, self.familia_nomo)).strip()

    def get_short_name(self):
        return self.persona_nomo

    def email_user(self, temo, mesagxo, sendulo=None):
        send_mail(temo, mesagxo, sendulo, [self.retposxto])
