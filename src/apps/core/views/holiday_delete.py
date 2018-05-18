from django.views.generic import DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.urls import reverse_lazy
from core.models.holidays import Holidays


class HolidayDelete(SuccessMessageMixin, DeleteView):
    model = Holidays
    template_name = 'core/holiday_delete.html'
    success_url = reverse_lazy('holiday')
    success_message = "%(name)s holiday was deleted successfully"

    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        messages.success(self.request, self.success_message % obj.__dict__)
        return super(HolidayDelete, self).delete(request, *args, **kwargs)
