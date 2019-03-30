from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from core.models.user import User


class CheckInUser(models.Model):
    employee = models.ForeignKey(User, on_delete=models.CASCADE)
    punchin = models.DateTimeField(_('check in'), null=True)
    punchout = models.DateTimeField(_('check out'), null=True)
    workhours = models.TimeField(_('work hours'), null=True)
