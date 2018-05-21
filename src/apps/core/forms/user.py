from django.forms import ModelForm, DateField
from django import forms
from django.conf import settings
from core.models.user import User


class UserRegisterForm(ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)
    birth_date = DateField(input_formats=settings.DATE_INPUT_FORMATS, required=True)
    first_name = forms.CharField(required=True, max_length=50)
    last_name = forms.CharField(required=True, max_length=50)

    class Meta:
        model = User
        fields = ('email', 'password1', 'password2', 'first_name', 'last_name', 'birth_date', 'gender')
