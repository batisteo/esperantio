from django.utils.translation import ugettext_lazy as _

class PublikoElektoj(object):
    CXIUJ, PLENKRESKULOJ, FAMILIOJ, JUNULOJ, INFANOJ = 0, 1, 2, 3, 4
    choices = (
        (CXIUJ, _("cxiuj")),
        (PLENKRESKULOJ, _("plenkreskuloj")),
        (FAMILIOJ, _("familioj")),
        (JUNULOJ, _("junuloj")),
        (INFANOJ, _("infanoj")),
    )

class OftecoElektoj(object):
    MALREGULE, TAGE, DUTAGE, FOJE_SEMAJNE, SEMAJNE, DUSEMAJNE = 0, 1, 2, 4, 7, 14
    MONATE, DUMONATE, SESMONATE, JARE, MALOFTE = 30, 61, 183, 365, 999
    choices = (
        (MALREGULE,_("malregule")),
        (TAGE,_("tage")),
        (DUTAGE,_("dutage")),
        (FOJE_SEMAJNE,_("foje semajne")),
        (SEMAJNE,_("semajne")),
        (DUSEMAJNE,_("dusemajne")),
        (MONATE,_("monate")),
        (DUMONATE,_("dumonate")),
        (SESMONATE,_("sesmonate")),
        (JARE,_("jare")),
        (MALOFTE,_("malofte")),
    )
