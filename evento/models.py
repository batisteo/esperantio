# -*- coding:utf-8 -*-
from datetime import datetime
from django.db import models
from django.utils.translation import ugettext_lazy as _

from .elektoj import SKALO_ELEKTOJ, TEMO_ELEKTOJ, PUBLIKO_ELEKTOJ

class Evento(models.Model):
    nomo = models.CharField(_("nomo"), max_length=255)
    longa_nomo = models.CharField(_("longa nomo"), max_length=255)
    # organizo = models.ForeignKey('evento.Organizo', verbose_name=_("organizo"))
    organizo = models.CharField(_("organizo"), max_length=255)
    retejo = models.URLField(_("retejo"))
    retposhto = models.EmailField(_("retposhto"))
    komenco = models.DateTimeField(_("komenco"))
    fino = models.DateTimeField(_("fino"))
    skalo = models.PositiveSmallIntegerField(_("skalo"), max_length=1, null=True,
                                        choices=SKALO_ELEKTOJ, default=0)
    temo = models.PositiveSmallIntegerField(_("temo"), max_length=1, null=True,
                                        choices=TEMO_ELEKTOJ, default=0)
    publiko = models.PositiveSmallIntegerField(_("publiko"), max_length=1, null=True,
                                        choices=PUBLIKO_ELEKTOJ, default=0)
    long = models.FloatField(_("longitudo"))
    lat = models.FloatField(_("latitudo"))
    nb_partopr = models.PositiveSmallIntegerField(_("nombro da partoprenantoj"))

    class Meta:
        verbose_name = _("evento")
        verbose_name_plural = _("eventoj")
    
    def __unicode__(self):
        return self.nomo
