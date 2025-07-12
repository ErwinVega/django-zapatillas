from django.db import models
from django.utils.translation import gettext_lazy as _


class SisesChoices(models.IntegerChoices):
    
    
    SISE_38 = 38, _('38')
    SISE_39 = 39, _('39')
    SISE_40 = 40, _('40')
    SISE_41 = 41, _('41')
    SISE_42 = 42, _('42')
    SISE_43 = 43, _('43')
    SISE_44 = 44, _('44')
    
    
    