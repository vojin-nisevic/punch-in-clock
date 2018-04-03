from django.views.generic import ListView
from core.models.models import MyProfile
from core.models.user import User


class Profile(ListView):
    model = User

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context

        context = super(Profile, self).get_context_data(**kwargs)

        # Create any data and add it to the context

        context['email'] = User.email
        context['name'] = User.first_name

        return context
