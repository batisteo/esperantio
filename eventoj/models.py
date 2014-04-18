# -*- coding:utf-8 -*-
from datetime import datetime
from django.db import models
from django.utils.translation import ugettext_lazy as _
from taggit.managers import TaggableManager

from django_countries.fields import CountryField
from django_extensions.db.models import TimeStampedModel

from .elektoj import PUBLIKO_ELEKTOJ, OFTECO_ELEKTOJ


class Arangxo(TimeStampedModel):
    kreanto = models.ForeignKey("uzantoj.Uzanto", verbose_name=_("Kreanto"))
    nomo = models.CharField(_("nomo de la renkontigxo"), max_length=255, unique=True)
    mallonga_nomo = models.CharField(_("mallonga nomo"), max_length=255, blank=True,
            help_text=_("Mallonga nomo se ekzistas."), unique=True)
    retejo = models.URLField(_("retejo"), blank=True)
    retposxto = models.EmailField(_("retposxto"), blank=True)
    organizo = models.ForeignKey('organizoj.Organizo', verbose_name=_("organizo"),
        blank=True, null=True)
    publiko = models.PositiveSmallIntegerField(_("publiko"),
                choices=PUBLIKO_ELEKTOJ, max_length=1, null=True, default=0)
    nb_partoprenantoj = models.PositiveIntegerField(_("nombro da partoprenantoj"),
            help_text="Proksimuma nombro de partoprenantoj.")
    etikedoj = TaggableManager(blank=True)
    ofteco = models.PositiveIntegerField(_("ofteco"), blank=True, null=True,
            help_text="Gxenerala ofteco de la renkontigxo.",
            choices=OFTECO_ELEKTOJ)
    dauro = models.PositiveIntegerField(_("dauxro"), blank=True, null=True,
            help_text="Gxenerala dauxro de la renkontigxo.")

    class Meta:
        verbose_name = _("arangxo")
        verbose_name_plural = _("arangxoj")

    def __unicode__(self):
        return self.nomo



class Evento(TimeStampedModel):
    kreanto = models.ForeignKey("uzantoj.Uzanto", verbose_name=_("Kreanto"))
    arangxo = models.ForeignKey("eventoj.Arangxo", verbose_name=_("Arangxo"))
    komenco = models.DateTimeField(_("komenco"))
    fino = models.DateTimeField(_("fino"), blank=True)
    temo = models.CharField(_("temo"), max_length=255, blank=True)
    adreso = models.CharField(_("adreso"), max_length=255, blank=True)
    adreso2 = models.CharField(_("adreso 2"), max_length=255, blank=True)
    urbo = models.CharField(_("urbo"), max_length=255, blank=True)
    posxtkodo = models.CharField(_("posxtkodo"), max_length=10, blank=True)
    lando = CountryField()
    lat = models.FloatField(_("latitudo"), null=True, blank=True)
    long = models.FloatField(_("longitudo"), null=True, blank=True)
    nb_partoprenantoj = models.PositiveIntegerField(_("nombro da partoprenantoj"),
            blank=True, null=True, help_text="Proksimuma nombro de partoprenantoj.")
    priskribo = models.TextField(_("priskribo"), blank=True, null=True)

    @property
    def jaro(self):
        return self.komenco.year
    

    class Meta:
        verbose_name = _("evento")
        verbose_name_plural = _("eventoj")

    def __unicode__(self):
        return self.arangxo.nomo + ' ' + str(self.jaro)

    def as_dict(self):
        return {'nomo': self.arangxo.nomo,
                'lat': self.lat,
                'long': self.long,
        }
