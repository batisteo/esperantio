from django.db import models
from django.utils.translation import ugettext_lazy as _

from django_countries.fields import CountryField
from django_extensions.db.models import TimeStampedModel

from uzantoj.models import Uzanto
from .elektoj import SKALO_ELEKTOJ

class Organizo(TimeStampedModel):
    nomo = models.CharField(_("nomo"), max_length=255)
    retejo = models.URLField(_("retejo"), blank=True)
    retposxto = models.EmailField(_("retposxto"), blank=True)
    twitter = models.CharField(_("twitter"), max_length=255, blank=True)
    vera_nomo_bezonata = models.BooleanField(_("vera nomo bezonata"), default=False)
    skalo = models.PositiveSmallIntegerField(_("skalo"),
                choices=SKALO_ELEKTOJ, null=True, default=0)

    adreso = models.CharField(_("adreso"), max_length=255, blank=True)
    adreso2 = models.CharField(_("adreso kont."), max_length=255, blank=True)
    posxtkodo = models.CharField(_("posxtkodo"), max_length=10, blank=True)
    urbo = models.CharField(_("urbo"), max_length=255, blank=True)
    lando = CountryField()

    uzantoj = models.ManyToManyField("uzantoj.Uzanto", verbose_name=_("uzantoj"))

    class Meta:
        verbose_name = _("organizo")
        verbose_name_plural = _("organizoj")

    def __str__(self):
        return self.nomo
