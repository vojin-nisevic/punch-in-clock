from django.views.generic import FormView
from django.conf import settings
from django.shortcuts import redirect
from django.core import mail
from core.forms.invite import InviteForm


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