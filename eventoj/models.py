# -*- coding:utf-8 -*-
from datetime import datetime
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.translation import ugettext_lazy as _

from autoslug.fields import AutoSlugField
from taggit.managers import TaggableManager

from django_countries.fields import CountryField
from django_extensions.db.models import TimeStampedModel

from .choices import PublikoElektoj, OftecoElektoj
from .constants import BASE_FACEBOOK_URL, BASE_TWITTER_URL


class Arangxo(TimeStampedModel):
    PUBLIKO_ELEKTOJ = PublikoElektoj
    OFTECO_ELEKTOJ = OftecoElektoj

    kreanto = models.ForeignKey("uzantoj.Uzanto", verbose_name=_("Kreanto"))
    nomo = models.CharField(_("nomo de la renkontigxo"), max_length=255, unique=True)
    mallonga_nomo = models.CharField(_("mallonga nomo"), blank=True,
            help_text=_("Mallonga nomo se ekzistas."), max_length=255)
    slug = AutoSlugField(_("ligila nomo"), populate_from="get_shorter_name", unique=True)
    retejo = models.URLField(_("retejo"), blank=True)
    retposxto = models.EmailField(_("retposxto"), blank=True)
    facebook = models.CharField(_("facebook identigilo"), max_length=255, blank=True,
            help_text=BASE_FACEBOOK_URL+"[...]")
    twitter = models.CharField(_("twitter identigilo"), max_length=255, blank=True,
            help_text=BASE_TWITTER_URL+"[...]")
    organizo = models.ForeignKey('organizoj.Organizo', verbose_name=_("organizo"),
        blank=True, null=True)
    publiko = models.PositiveSmallIntegerField(_("publiko"),
            choices=PUBLIKO_ELEKTOJ.choices, max_length=1, null=True, default=0)
    min_homoj = models.PositiveIntegerField(_("minimuma nombro da partoprenantoj"))
    max_homoj = models.PositiveIntegerField(_("maksimuma nombro da partoprenantoj"))
    etikedoj = TaggableManager(blank=True)
    ofteco = models.PositiveIntegerField(_("ofteco"), blank=True, null=True,
            help_text="Gxenerala ofteco de la renkontigxo.",
            choices=OFTECO_ELEKTOJ.choices)
    dauro = models.PositiveIntegerField(_("dauxro"), blank=True, null=True,
            help_text="Gxenerala dauxro de la renkontigxo, en tagoj.")

    @property
    def facebook_url(self):
        return BASE_FACEBOOK_URL + self.facebook if self.facebook else ''

    @property
    def twitter_url(self):
        return BASE_TWITTER_URL + self.twitter if self.twitter else ''

    class Meta:
        verbose_name = _("arangxo")
        verbose_name_plural = _("arangxoj")

    def __unicode__(self):
        return self.nomo

    def get_shorter_name(self):
        return self.mallonga_nomo if self.mallonga_nomo else self.nomo



class Evento(TimeStampedModel):
    kreanto = models.ForeignKey("uzantoj.Uzanto", verbose_name=_("Kreanto"))
    arangxo = models.ForeignKey("eventoj.Arangxo", verbose_name=_("Arangxo"),
            related_name="eventoj")
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
    priskribo = models.TextField(_("priskribo"), blank=True, null=True)

    @property
    def jaro(self):
        return self.komenco.year

    @property
    def monato(self):
        return self.komenco.month

    @property
    def tago(self):
        return self.komenco.day
    

    class Meta:
        verbose_name = _("evento")
        verbose_name_plural = _("eventoj")

    def __unicode__(self):
        return self.arangxo.nomo + ' ' + str(self.jaro)

    def get_absolute_url(self):
        return reverse('evento_detail', kwargs={
            'slug': self.arangxo.slug,
            'jaro': self.komenco.year,
            'monato': self.komenco.month,
            'tago': self.komenco.day,
        })

    def as_dict(self):
        return {
                'id': self.pk,
                'nomo': self.arangxo.nomo,
                'mallonga_nomo': self.arangxo.mallonga_nomo,
                'jaro': self.jaro,
                'komenco': str(self.komenco),
                'fino': str(self.fino),
                'temo': self.temo,
                'lat': self.lat,
                'long': self.long,
                'urbo': self.urbo,
                'url': self.get_absolute_url()
        }
