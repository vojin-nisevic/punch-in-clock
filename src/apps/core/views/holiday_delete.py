from django.views.generic import DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from core.models.holidays import Holidays


class HolidayDelete(SuccessMessageMixin, DeleteView):
    model = Holidays
    template_name = 'holiday_delete.html'
    success_url = reverse_lazy('holiday')
    success_message = "%(name)s holiday was deleted successfully"
