# from django.contrib.auth.models import User
from django.db import models
from core.models.user import User


class MyProfile(models.Model):
    user = User.username
