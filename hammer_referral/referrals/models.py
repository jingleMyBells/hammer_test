from django.conf import settings
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models

from referrals.managers import CustomUserManager
from referrals.validators import PhoneNumberValidator


class User(AbstractBaseUser, PermissionsMixin):
    phone = models.CharField(
        'phone_number',
        unique=True,
        max_length=settings.PHONE_MAX_LENGTH,
        validators=[PhoneNumberValidator],
        error_messages={
            'unique': 'Phone number is already taken',
        }
    )
    invitation_code = models.CharField(
        'invitation_code',
        max_length=settings.REFERRER_CODE_MAX_LENGTH,
        null=True,
    )
    referrer_code = models.CharField(
        'referrer_code',
        max_length=settings.REFERRER_CODE_MAX_LENGTH,
        null=False,
        blank=False,
        unique=True,
    )
    is_active = models.BooleanField('active', default=True)
    objects = CustomUserManager()

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    def get_full_name(self):
        return self.phone

    def get_short_name(self):
        return self.phone
