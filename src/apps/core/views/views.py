from django.views.generic import UpdateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy, reverse
from core.models.user import User
from django.utils.module_loading import import_module
from django.http import HttpRequest, HttpResponseRedirect
from django.conf import settings
from django.contrib.auth import logout



@method_decorator(login_required, name='dispatch')
class Profile(UpdateView):
    model = User
    template_name = 'profile.html'
    fields = ['first_name', 'last_name', 'birth_date', 'gender', 'profile_image', 'address', 'zip', 'city', 'state_province',
              'country', 'home_phone', 'desk_phone', 'cell_phone']

    def get_success_url(self):
        return reverse_lazy('profile', args=(self.pk_url_kwarg,))

    def get_object(self, queryset=None):
        """

        With returning current user object we prevent users from updating other user profiles.



        :param queryset:

        :return: object User from request

        """

        return self.request.user


def logout(self):
    """
    Removes the authenticated user's cookies and session object.

    Causes the authenticated user to be logged out.
    """
    from django.contrib.auth import get_user, logout
    request = HttpRequest()
    engine = import_module(settings.SESSION_ENGINE)
    if self.session:
        request.session = self.session
        request.user = get_user(request)
    else:
        request.session = engine.SessionStore()
    logout(request)
    url = reverse('login',)
    return HttpResponseRedirect(url)
    # return reverse_lazy('login')
