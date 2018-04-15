from django.views.generic import UpdateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from core.models.user import User
from core.forms.forms import UserForm


@method_decorator(login_required, name='dispatch')
class Profile(UpdateView):
    model = User
    form_class = UserForm
    template_name = 'profile.html'
    # fields = ['first_name', 'last_name', 'birth_date', 'gender', 'profile_image', 'address',
    # 'zip', 'city', 'state_province',
    # 'country', 'home_phone', 'desk_phone', 'cell_phone']

    def get_success_url(self):
        return reverse_lazy('profile', args=(self.pk_url_kwarg,))

    def get_object(self, queryset=None):
        """

        With returning current user object we prevent users from updating other user profiles.



        :param queryset:

        :return: object User from request

        """

        return self.request.user
