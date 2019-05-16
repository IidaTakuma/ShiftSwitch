from django.contrib import auth
from django.contrib.auth.models import UserManager,PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.contenttypes.models import ContentType
from django.core.exceptions import PermissionDenied
from django.core.mail import send_mail
from django.db import models
from django.db.models.manager import EmptyManager
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.validators import UnicodeUsernameValidator

# Create your models here.

class UserManager(BaseUserManager):
  
    use_in_migrations = True
  
    def _create_user(self, email, password, **extra_fields):
        """Create and save a user with the given username, email, and
        password."""
        if not email:
            raise ValueError('The given email must be set')

        domain = email.split('@')
        print(domain[1])
        # if domain[1] not "ca-techkids.com":
        #     raise ValueError('ドメインがca-techkids.comのものしか登録できません')

        email = self.normalize_email(email)
  
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
  
    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)
  
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
  
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
  
        return self._create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    """
    Username and password are required. Other fields are optional.
    """
    username = models.CharField(max_length=30, verbose_name='メンター名', blank=True)
    email = models.EmailField(_('email address'),unique=True,)
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_('Designates whether the user can log into this admin site.'),
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    full_name = models.CharField(_('氏名'), max_length=150, blank=True)

    objects = UserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def get_full_name(self):
        return self.full_name

    def get_short_name(self):
        return self.full_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        """Send an email to this user."""
        send_mail(subject, message, from_email, [self.email], **kwargs)

# class Activate(models.Model):
#     """ 仮登録したユーザを本登録するためのModel """
  
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     key = models.CharField(max_length=255, unique=True)
#     expiration_date = models.DateTimeField(blank=True, null=True)