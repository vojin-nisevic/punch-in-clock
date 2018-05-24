from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from core.models.user import Department
from core.forms.department import DepartmentForm


class Departmentslist(ListView):
    model = Department
    template_name = 'department.html'
    Department.context_object_name = 'department_list'

    def get_allow_empty(self):
        return self.allow_empty

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = Department.name
        return context


class DepartmentCreate(CreateView):
    model = Department
    fields = ['manager', 'name', 'building', 'phone', 'email']

    def get_success_url(self):
        return reverse_lazy('department')


class DepartmentDelete(DeleteView):
    model = Department
    template_name = 'department_delete.html'

    def get_success_url(self):
        return reverse_lazy('department')

    def get_object(self, queryset=None):
        obj = super(DepartmentDelete, self).get_object()
        return obj


class DepartmentUpdate(UpdateView):
    model = Department
    template_name = 'department-UD.html'
    form_class = DepartmentForm

    def get_success_url(self):
        return reverse_lazy('department')
