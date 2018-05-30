from django.views.generic import ListView, DeleteView, CreateView, UpdateView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from core.models.free_days import FreeDays
from core.forms.free_days import FreeDaysForm
from core.views.security import *


class FreeDaysList(UserManagerTest, ListView):
    model = FreeDays
    FreeDays.context_object_name = 'freedays_list'


class FreeDaysCreate(UserManagerTest, SuccessMessageMixin, CreateView):
    model = FreeDays
    form_class = FreeDaysForm
    success_url = reverse_lazy('freedays')
    success_message = '%(name)s was created successfully'


class FreeDaysDelete(UserManagerTest, SuccessMessageMixin, DeleteView):
    model = FreeDays
    success_url = reverse_lazy('freedays')
    success_message = '%(name)s was deleted successfully'

    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        messages.success(self.request, self.success_message %obj.__dict__)
        return super(FreeDaysDelete, self).delete(request, *args, **kwargs)


class FreeDaysUpdate(UserManagerTest, SuccessMessageMixin, UpdateView):
    model = FreeDays
    success_url = reverse_lazy('freedays')
    success_message = '%(name)s was updated successfully'
    template_name = 'core/freedays_update.html'
    form_class = FreeDaysForm
