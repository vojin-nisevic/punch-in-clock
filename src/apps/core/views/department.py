from django.views.generic import ListView
from core.models.user import Department


class Departments(ListView):
    model = Department
    template_name = 'department.html'
    Department.context_object_name = 'department_list'

    def get_allow_empty(self):
        return self.allow_empty

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = Department.name
        return context


