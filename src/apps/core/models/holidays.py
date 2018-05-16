from django.db import models
from django.utils.translation import ugettext_lazy as _


class Holidays(models.Model):
    HOLIDAYS = (
        ('N', 'National'),
        ('L', 'Local'),
        ('R', 'Religious'),
    )
    name = models.CharField(_('name'), max_length=100)
    holiday_type = models.CharField(_('type'), choices=HOLIDAYS, max_length=1)
    date = models.DateField(_('date'))
