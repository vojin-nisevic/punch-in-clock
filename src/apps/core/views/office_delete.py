from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from core.models.user import Office


class OfficeDelete(DeleteView):
    model = Office
    template_name = 'office_delete.html'

    def get_success_url(self):
        return reverse_lazy('office')

    def get_object(self, queryset=None):
        obj = super(OfficeDelete, self).get_object()
        return obj
