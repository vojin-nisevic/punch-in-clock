from django.views.generic import ListView
from django.urls import reverse_lazy
from core.forms.department import DepartmentForm
from core.models.user import Department


class Departments(ListView):
    model = Department
    # form_class = DepartmentForm
    template_name = 'department.html'
    Department.context_object_name = 'department_list'

    def get_allow_empty(self):
        return self.allow_empty

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = Department.name
        return context

    def post(self):
        return reverse_lazy('department-UD', args=self.request.POST)

    # def get(self, request, *args, **kwargs):
    #     pass
    # return reverse_lazy('department-UD', kwargs.keys())


