from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.translation import ugettext_lazy as _


class FreeDays(models.Model):
    FREE_DAYS = (
        ('AD', 'Administrative days'),
        ('FC', 'Family care days'),
        ('FU', 'Funeral days'),
    )
    name = models.CharField(_('name'), max_length=50)
    type = models.CharField(_('type'), choices=FREE_DAYS, max_length=2)
    duration = models.IntegerField(_('duration'),
                                   validators=[MaxValueValidator(10, 'Cannot be greater then 10'),
                                               MinValueValidator(0, 'Cannot be less then zero')])

