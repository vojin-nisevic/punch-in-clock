from django.forms import ModelForm, DateField
from core.models.user import User
from django.conf import settings


class UserForm(ModelForm):
    birth_date = DateField(input_formats=settings.DATE_INPUT_FORMATS)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'gender', 'birth_date', 'address',
                  'zip', 'city', 'state_province', 'country', 'home_phone',
                  'desk_phone', 'cell_phone', 'facebook', 'linkedin',
                  'twitter', 'profile_image')


