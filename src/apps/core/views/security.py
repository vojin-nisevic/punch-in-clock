from django.contrib.auth.mixins import UserPassesTestMixin


class UserManagerTest(UserPassesTestMixin):

    def test_func(self):
        return self.request.user.is_manager