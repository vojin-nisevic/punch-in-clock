from django.shortcuts import render
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy, reverse
from django.utils.translation import ugettext_lazy as _
from django.views.generic import FormView
from django.http import  HttpResponseRedirect
from django.contrib import messages
from core.forms.user import UserRegisterForm
from core.views.security import *


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
            messages.add_message(request, messages.INFO, self.success_message)
            return HttpResponseRedirect(reverse('home'))
