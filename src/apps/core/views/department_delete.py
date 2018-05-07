from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from core.models.user import Department


class DepartmentDelete(DeleteView):
    model = Department
    template_name = 'department_delete.html'

    def get_success_url(self):
        return reverse_lazy('department')

    def get_object(self, queryset=None):
        obj = super(DepartmentDelete, self).get_object()
        return obj
