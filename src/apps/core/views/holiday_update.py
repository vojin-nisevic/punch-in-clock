from django.views.generic import UpdateView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from core.models.holidays import Holidays
from core.forms.holidays import HolidayForm


class HolidayUpdate(SuccessMessageMixin, UpdateView):
    model = Holidays
    form_class = HolidayForm
    success_url = reverse_lazy('holiday')
    template_name = 'core/holiday_update.html'
    success_message = "%(name)s holiday was updated successfully"
