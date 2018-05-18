from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from core.models.user import Office


class OfficeCreate(SuccessMessageMixin, CreateView):
    model = Office
    fields = ['name', 'building']
    success_message = "%(name)s office was created successfully"

    def get_success_url(self):
        return reverse_lazy('office')
