from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from core.forms.holidays import HolidayForm
from core.models.holidays import Holidays


class HolidayCreate(SuccessMessageMixin, CreateView):
    model = Holidays
    form_class = HolidayForm
    success_url = reverse_lazy('holiday')
    success_message = "%(name)s holiday was created successfully"
