from django.forms import ModelForm
from core.models.holidays import Holidays


class HolidayForm(ModelForm):

    class Meta:
        model = Holidays
        fields = ('name', 'holiday_type', 'date')
