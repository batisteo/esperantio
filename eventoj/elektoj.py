# -*- coding:utf-8 -*-
from django.utils.translation import ugettext_lazy as _


MONDO, KONTINENTO, LANDO, REGIONO, URBO = 0, 1, 2, 3, 4
SKALO_ELEKTOJ = (
    (MONDO, _("mondo")),
    (KONTINENTO, _("kontinento")),
    (LANDO, _("lando")),
    (REGIONO, _("regiono")),
    (URBO, _("urbo")),
)


GXENERALA, STUDADA, KULTURA, FERVOJISTA = 0, 1, 2, 3
TEMO_ELEKTOJ = (
    (GXENERALA, _("gxenerala")),
    (STUDADA, _("studada")),
    (KULTURA, _("kultura")),
    (FERVOJISTA, _("fervojista")),
)


CXIUJ, JUNULOJ, MALJUNULOJ = 0, 1, 2
PUBLIKO_ELEKTOJ = (
    (CXIUJ, _("cxiuj")),
    (JUNULOJ, _("junuloj")),
    (MALJUNULOJ, _("maljunuloj")),
)

NB_PARTOPR_ELEKTOJ = (
    (5, _("5")),
    (20, _("20")),
    (50, _("50")),
    (100, _("100")),
    (200, _("200")),
    (500, _("500")),
    (1000, _("1000")),
)
