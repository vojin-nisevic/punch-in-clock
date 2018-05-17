from django.forms import ModelForm
from core.models.free_days import FreeDays


class FreeDaysForm(ModelForm):

    class Meta:
        model = FreeDays
        fields = ('name', 'type', 'duration')
