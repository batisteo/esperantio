from django.db import models
from django.utils.translation import ugettext_lazy as _

class Evento(models.Model):
    nomo = models.CharField(_("nomo"), max_length=255)
    longa_nomo = models.CharField(_("longa nomo"), max_length=255)
    # organizo = models.ForeignKey('evento.Organizo', verbose_name=_("organizo"))
    organizo = models.CharField(_("organizo"), max_length=255)
    retejo = models.URLField(_("retejo"))
    retposhto = models.EmailField(_("retposhto"))
    komenco = models.DateTimeField(_("komenco"))
    fino = models.DateTimeField(_("fino"))
    skalo = models.PositiveSmallIntegerField(_("skalo"))
    temo = models.PositiveSmallIntegerField(_("temo"))
    publiko = models.PositiveSmallIntegerField(_("publiko"))
    long = models.FloatField(_("longitudo"))
    lat = models.FloatField(_("latitudo"))
    nb_partopr = models.PositiveSmallIntegerField(_("nombro da partoprenantoj"))

    class Meta:
        verbose_name = _("evento")
        verbose_name_plural = _("eventoj")
