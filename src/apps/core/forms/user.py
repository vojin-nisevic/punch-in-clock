from django.forms import ModelForm, DateField, ModelChoiceField
from django import forms
from django.conf import settings
from core.models.user import User, Department


class UserRegisterForm(ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)
    birth_date = DateField(input_formats=settings.DATE_INPUT_FORMATS, required=True)
    first_name = forms.CharField(required=True, max_length=50)
    last_name = forms.CharField(required=True, max_length=50)

    class Meta:
        model = User
        fields = ('email', 'password1', 'password2', 'first_name', 'last_name', 'birth_date', 'gender')



class UserUpdateForm(ModelForm):
    department = ModelChoiceField(queryset=Department.objects.all().order_by('name'))

    class Meta:
        model = User
        fields = ('id', 'is_manager', 'department', 'position', 'address', 'city', 'zip', 'state_province', 'country', 'gender',
                  'first_name', 'last_name', 'home_phone', 'cell_phone', 'desk_phone')
