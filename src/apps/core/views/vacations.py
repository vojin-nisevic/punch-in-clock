from django.views.generic import CreateView, DeleteView, UpdateView, DetailView
from django.utils.translation import ugettext_lazy as _
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.urls import reverse_lazy
from core.views.security import *
from core.forms.vacation import *
from core.models.vacations import *


class VacationEmployeeCreate(UserManagerTest, SuccessMessageMixin, DetailView):
    model = VacationEmployee
    form_class = VacationEmployeeForm
    template_name = 'core/vacation_set.html'
    # success_message = _('You have successfully set vacations days')
    # success_url = reverse_lazy('users-list')
