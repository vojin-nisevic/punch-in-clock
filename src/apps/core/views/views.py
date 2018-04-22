from django.views.generic import UpdateView, FormView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from django.conf import settings
from django.shortcuts import redirect
from django.core import mail
from core.models.user import User
from core.forms.forms import UserForm, InviteForm


@method_decorator(login_required, name='dispatch')
class Profile(UpdateView):
    model = User
    form_class = UserForm
    template_name = 'profile.html'

    def get_success_url(self):
        return reverse_lazy('profile', args=(self.pk_url_kwarg,))

    def get_object(self, queryset=None):
        """

        With returning current user object we prevent users from updating other user profiles.



        :param queryset:

        :return: object User from request

        """

        return self.request.user


class Invite(FormView):
    form_class = InviteForm
    template_name = 'invite.html'

    def form_valid(self, form):
        subject = form.cleaned_data['subject']
        message = form.cleaned_data['message']
        from_email = settings.DEFAULT_FROM_EMAIL
        to_email = form.cleaned_data['recipient']
        with mail.get_connection() as connection:
            mail.EmailMessage(subject, message, from_email, [to_email], connection=connection).send(fail_silently=False)
        return redirect('home')


