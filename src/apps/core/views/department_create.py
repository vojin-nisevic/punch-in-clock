from django.views.generic.edit import CreateView
from django.urls import reverse
from core.models.user import Department


class DepartmentCreate(CreateView):
    model = Department
    fields = ['manager', 'name', 'building', 'phone', 'email']

    def get_success_url(self):
        return reverse('department')
