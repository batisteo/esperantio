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


GHENERALA, STUDADA, KULTURA, FERVOJISTA = 0, 1, 2, 3
TEMO_ELEKTOJ = (
    (GHENERALA, _("ĝenerala")),
    (STUDADA, _("studada")),
    (KULTURA, _("kultura")),
    (FERVOJISTA, _("fervojista")),
)


CHIUJ, JUNULOJ, MALJUNULOJ = 0, 1, 2
PUBLIKO_ELEKTOJ = (
    (CHIUJ, _("ĉiuj")),
    (JUNULOJ, _("junuloj")),
    (MALJUNULOJ, _("maljunuloj")),
)

