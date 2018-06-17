from django.forms import ModelForm, DateField
from django.conf import settings
from core.models.vacations import *


class VacationEmployeeForm(ModelForm):

    class Meta:
        model = VacationEmployee
        fields = ('employee', 'vacation_days', 'vacation_remainder')


class VacationUsedForm(ModelForm):
    vacation_start = DateField(input_formats=settings.DATE_INPUT_FORMATS)
    vacation_end = DateField(input_formats=settings.DATE_INPUT_FORMATS)

    class Meta:
        model = VacationUsed
        fields = ('employee', 'vacation_start', 'vacation_end')
