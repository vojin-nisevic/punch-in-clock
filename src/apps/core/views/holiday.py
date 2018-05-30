from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.contrib import messages
from core.views.security import *
from core.models.holidays import Holidays
from core.forms.holidays import HolidayForm


class ManagerTest(UserManagerTest, UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_manager

    login_url = 'home'


class HolidaysList(UserManagerTest, ListView):
    model = Holidays
    Holidays.context_object_name = 'holidays_list'
    ordering = ['date']


class HolidayCreate(UserManagerTest, SuccessMessageMixin, CreateView):
    model = Holidays
    form_class = HolidayForm
    success_url = reverse_lazy('holiday')
    success_message = "%(name)s holiday was created successfully"


class HolidayDelete(UserManagerTest, SuccessMessageMixin, DeleteView):
    model = Holidays
    template_name = 'core/holiday_delete.html'
    success_url = reverse_lazy('holiday')
    success_message = "%(name)s holiday was deleted successfully"

    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        messages.success(self.request, self.success_message % obj.__dict__)
        return super(HolidayDelete, self).delete(request, *args, **kwargs)


class HolidayUpdate(UserManagerTest, SuccessMessageMixin, UpdateView):
    model = Holidays
    form_class = HolidayForm
    success_url = reverse_lazy('holiday')
    template_name = 'core/holiday_update.html'
    success_message = "%(name)s holiday was updated successfully"
