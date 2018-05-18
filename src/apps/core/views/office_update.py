from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from core.models.user import Office
from core.forms.office import OfficeForm


class OfficeUpdate(UpdateView):
    model = Office
    template_name = 'office_update.html'
    form_class = OfficeForm

    def get_success_url(self):
        return reverse_lazy('office')
