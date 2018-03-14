"""
Custom User Model

"""

from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django_countries.fields import CountryField
from django.utils.translation import ugettext_lazy as _
from core import choices
from timezone_field import TimeZoneField


class UserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


def user_directory_path(instance, filename):
    # File will be uploaded to MEDIA_ROOT/user_profiles/<id>/<filename>
    return 'user_profiles/{0}/{1}'.format(instance.id, filename)


class Department(models.Model):
    name = models.CharField(_('department'), max_length=100)
    phone = models.CharField(max_length=100, blank=True)
    email = models.EmailField(max_length=100, blank=True)
    manager = models.CharField(_('manager'), max_length=100, blank=True)
    building = models.CharField(_('building'), max_length=100, blank=True)

    def __str__(self):
        return self.name


class Office(models.Model):
    name = models.CharField(_('office name'), max_length=100)
    building = models.CharField(_('building'), max_length=100, blank=True)

    def __str__(self):
        return self.name


class User(AbstractUser):
    """User model."""

    username = None
    email = models.EmailField(_('email address'), unique=True)

    is_manager = models.BooleanField(
        _('manager status'),
        default=False,
        help_text=_('Designates whether the user is manager or not.'),
    )

    department = models.ForeignKey('self', on_delete=models.CASCADE, related_name='department_set')
    office = models.ForeignKey('self', on_delete=models.CASCADE, related_name='office_set')
    position = models.CharField(_('position'), max_length=30, blank=True)
    birth_date = models.DateField(_('birth date'))
    gender = models.CharField(_('home phone'), max_length=1, choices=choices.MALE_OR_FEMALE)
    profile_image = models.ImageField(upload_to=user_directory_path)
    address = models.CharField(_('address'), max_length=50)
    zip = models.CharField(_('zip'), max_length=20)
    city = models.CharField(_('city'), max_length=30)
    state_province = models.CharField(_('state province'), max_length=50, blank=True)
    country = CountryField()
    home_phone = models.CharField(_('home phone'), max_length=20, blank=True)
    desk_phone = models.CharField(_('desk phone'), max_length=20, blank=True)
    cell_phone = models.CharField(_('cell phone'), max_length=20)
    facebook = models.URLField(_('facebook'), max_length=200, blank=True)
    linkedin = models.URLField(_('linkedin'), max_length=200, blank=True)
    twitter = models.URLField(_('twitter'), max_length=200, blank=True)
    timezone = TimeZoneField()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()
