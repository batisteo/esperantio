# -*- coding:utf-8 -*-
from datetime import datetime
from django.db import models
from django.utils.translation import ugettext_lazy as _
from taggit.managers import TaggableManager

from .elektoj import PUBLIKO_ELEKTOJ


class Arangxo(models.Model):
    nomo = models.CharField(_("nomo"), max_length=255)
    longa_nomo = models.CharField(_("longa nomo"), max_length=255, blank=True)
    retejo = models.URLField(_("retejo"), blank=True)
    retposxto = models.EmailField(_("retposxto"), blank=True)
    organizo = models.ForeignKey('organizoj.Organizo', verbose_name=_("organizo"),
        blank=True, null=True)
    publiko = models.PositiveSmallIntegerField(_("publiko"),
                choices=PUBLIKO_ELEKTOJ, max_length=1, null=True, default=0)
    nb_partoprenantoj = models.PositiveIntegerField(_("nombro da partoprenantoj"),
            help_text="Proksimuma nombro de partoprenantoj.")
    etikedoj = TaggableManager()

    class Meta:
        verbose_name = _("arangxo")
        verbose_name_plural = _("arangxoj")

    def __unicode__(self):
        return self.nomo



class Evento(models.Model):
    arangxo = models.ForeignKey("eventoj.Arangxo", verbose_name=_("Arangxo"))
    komenco = models.DateTimeField(_("komenco"))
    fino = models.DateTimeField(_("fino"), blank=True)
    adreso = models.CharField(_("adreso"), max_length=255)
    adreso2 = models.CharField(_("adreso kont."), max_length=255, blank=True)
    posxtkodo = models.CharField(_("posxtkodo"), max_length=10, blank=True)
    urbo = models.CharField(_("urbo"), max_length=255, blank=True)
    lando = models.CharField(_("lando"), max_length=255, blank=True)
    lat = models.FloatField(_("latitudo"), null=True, blank=True)
    long = models.FloatField(_("longitudo"), null=True, blank=True)
    nb_partoprenantoj = models.PositiveIntegerField(_("nombro da partoprenantoj"),
            blank=True, null=True, help_text="Proksimuma nombro de partoprenantoj.")
    priskribo = models.TextField(_("priskribo"), blank=True, null=True)
    

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
