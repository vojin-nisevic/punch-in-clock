from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from django.utils.translation import ugettext_lazy as _
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from core.models.user import Office
from core.forms.office import OfficeForm


class OfficesList(ListView):
    model = Office
    template_name = 'office.html'
    Office.context_object_name = 'office_list'
    ordering = ['name']


class OfficeCreate(SuccessMessageMixin, CreateView):
    model = Office
    fields = ['name', 'building']
    success_message = _("%(name)s office was created successfully")
    success_url = reverse_lazy('office')



class OfficeDelete(SuccessMessageMixin, DeleteView):
    model = Office
    template_name = 'office_delete.html'
    success_url = reverse_lazy('office')
    success_message = _("%(name)s office was deleted successfully")

    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        messages.success(self.request, self.success_message %obj.__dict__)
        return super(OfficeDelete, self).delete(request, *args, **kwargs)


class OfficeUpdate(SuccessMessageMixin, UpdateView):
    model = Office
    template_name = 'office_update.html'
    form_class = OfficeForm
    success_url = reverse_lazy('office')
    success_message = _('%(name)s office was successfully updated')
