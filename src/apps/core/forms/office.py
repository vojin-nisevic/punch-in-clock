from django.forms import ModelForm
from core.models.user import Office


class OfficeForm(ModelForm):

    class Meta:
        model = Office
        fields = ('name', 'building')
