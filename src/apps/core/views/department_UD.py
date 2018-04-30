from django.views.generic.edit import UpdateView
from django.urls import reverse
from core.models.user import Department
from core.forms.department import DepartmentForm


class DepartmentUpdate(UpdateView):
    model = Department
    template_name = 'department-UD.html'
    form_class = DepartmentForm

    def get_success_url(self):
        return reverse('department')
