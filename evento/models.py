# -*- coding:utf-8 -*-
from datetime import datetime
from django.db import models
from django.utils.translation import ugettext_lazy as _

from .elektoj import SKALO_ELEKTOJ, TEMO_ELEKTOJ, PUBLIKO_ELEKTOJ, NB_PARTOPR_ELEKTOJ


class Arangxo(models.Model):
    nomo = models.CharField(_("nomo"), max_length=255)
    longa_nomo = models.CharField(_("longa nomo"), max_length=255, blank=True)
    # organizo = models.ForeignKey('evento.Organizo', verbose_name=_("organizo"))
    organizo = models.CharField(_("organizo"), max_length=255, blank=True)
    skalo = models.PositiveSmallIntegerField(_("skalo"),
                choices=SKALO_ELEKTOJ, max_length=1, null=True, default=0)
    temo = models.PositiveSmallIntegerField(_("temo"),
                choices=TEMO_ELEKTOJ, max_length=1, null=True, default=0)
    publiko = models.PositiveSmallIntegerField(_("publiko"),
                choices=PUBLIKO_ELEKTOJ, max_length=1, null=True, default=0)

    class Meta:
        verbose_name = _("arangxo")
        verbose_name_plural = _("arangxoj")

    def __unicode__(self):
        return self.nomo



class Evento(models.Model):
    arangxo = models.ForeignKey("evento.Arangxo", verbose_name=_("Arangxo"))
    retejo = models.URLField(_("retejo"), blank=True)
    retposxto = models.EmailField(_("retposxto"), blank=True)
    komenco = models.DateTimeField(_("komenco"), blank=True)
    fino = models.DateTimeField(_("fino"))
    adreso = models.CharField(_("adreso"), max_length=255)
    adreso2 = models.CharField(_("adreso kont."), max_length=255, blank=True)
    posxtkodo = models.CharField(_("posxtkodo"), max_length=10, blank=True)
    urbo = models.CharField(_("urbo"), max_length=255, blank=True)
    lando = models.CharField(_("lando"), max_length=255, blank=True)
    lat = models.FloatField(_("latitudo"), null=True, blank=True)
    long = models.FloatField(_("longitudo"), null=True, blank=True)
    nb_partopr = models.PositiveSmallIntegerField(_("nombro da partoprenantoj"),
                choices=NB_PARTOPR_ELEKTOJ, null=True, blank=True)

    class Meta:
        verbose_name = _("evento")
        verbose_name_plural = _("eventoj")

    def __unicode__(self):
        return self.arangxo.nomo

    def as_dict(self):
        return {'nomo': self.arangxo.nomo,
                'lat': self.lat,
                'long': self.long,
        }

    @property
    def jaro(self):
        return self.komenco.year
