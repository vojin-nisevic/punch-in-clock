from django.shortcuts import render
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy, reverse
from django.utils.translation import ugettext_lazy as _
from django.views.generic import FormView, ListView, DetailView, UpdateView
from django.http import  HttpResponseRedirect
from django.contrib import messages
from django.conf import settings
from core.forms.user import *
from core.views.security import *
from core.models.user import User
from core.models.vacations import *


class UserRegister(UserManagerTest, SuccessMessageMixin, FormView):

    form_class = UserRegisterForm
    template_name = 'core/user_register.html'
    success_url = reverse_lazy('home')
    success_message = _('Employee account was successfully created')

    def get(self, request, *args, **kwargs):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(self.request.POST)
        if form.is_valid():
            pass1 = form.cleaned_data['password1']
            pass2 = form.cleaned_data['password2']
            if pass1 != pass2:
                form.errors['password1'] = _('Passwords do not mach!')
                return render(request, self.template_name, {'form': form})
            user = form.save(commit=False)
            user.set_password(pass1)
            user.username = form.cleaned_data['email']
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.birth_date = form.cleaned_data['birth_date']
            user.gender = form.cleaned_data['gender']
            user.save()
            ve = VacationEmployee(employee_id=user.id, vacation_days=25, vacation_remainder=25)
            ve.save()
            settings.configure(VACATION_DAYS=25)
            messages.add_message(request, messages.INFO, self.success_message)
            return HttpResponseRedirect(reverse('users-list'))


class UsersList(UserManagerTest, ListView):
    model = User
    context_object_name = 'users_list'
    template_name = 'core/users_list.html'
    ordering = ('last_name', 'first_name',)
    queryset = User.objects.filter(is_superuser=False)


class UserUpdate(UserManagerTest, SuccessMessageMixin, UpdateView):
    form_class = UserUpdateForm
    template_name = 'core/user_update.html'
    model = User
    success_message = _('Employee account was successfully created')
    success_url = reverse_lazy('users-list')

    def get_object(self, queryset=None):
        obj = super(UserUpdate, self).get_object()
        return obj
