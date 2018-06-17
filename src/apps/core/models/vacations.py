from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.validators import MaxValueValidator
from core.models.user import User


class VacationEmployee(models.Model):
    employee = models.OneToOneField(User, on_delete=models.CASCADE, related_name='vacation')
    vacation_days = models.PositiveIntegerField(_('vacation_days'), default=25, validators=[MaxValueValidator(50)])
    vacation_remainder = models.PositiveIntegerField(_('vacation_remainder'), default=25)


class VacationUsed(models.Model):
    employee = models.ForeignKey(User, on_delete=models.CASCADE, related_name='vacation_used')
    start_vacation = models.DateField(_('start_vacation'), unique_for_date=True)
    end_vacation = models.DateField(_('end_vacation'), unique_for_date=True)
