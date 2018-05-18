from django.forms import ModelForm
from core.models.user import Department


class DepartmentForm(ModelForm):

    class Meta:
        model = Department
        fields = ('manager', 'name', 'building', 'phone', 'email')
