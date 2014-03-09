from django.db import models
from django.utils.translation import ugettext_lazy as _

from uzantoj.models import Uzanto
from .elektoj import SKALO_ELEKTOJ

class Organizo(models.Model):
    nomo = models.CharField(_("nomo"), max_length=255)
    retejo = models.URLField(_("retejo"), blank=True)
    retposxto = models.EmailField(_("retposxto"), blank=True)
    vera_nomo_bezonata = models.BooleanField(_("vera nomo bezonata"))
    skalo = models.PositiveSmallIntegerField(_("skalo"),
                choices=SKALO_ELEKTOJ, max_length=1, null=True, default=0)

    uzantoj = models.ManyToManyField("uzantoj.Uzanto", verbose_name=_("uzantoj"))

    class Meta:
        verbose_name = _("organizo")
        verbose_name_plural = _("organizoj")

    def __unicode__(self):
        return self.nomo
