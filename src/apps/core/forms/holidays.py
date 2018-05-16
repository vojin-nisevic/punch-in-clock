from django.forms import ModelForm, DateField
from django.conf import settings
from core.models.holidays import Holidays


class HolidayForm(ModelForm):
    # date = DateField(input_formats=settings.DATE_INPUT_FORMATS)

    class Meta:
        model = Holidays
        fields = ('name', 'holiday_type', 'date')
