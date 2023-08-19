from django.conf import settings
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models

from referrals.managers import CustomUserManager
from referrals.validators import PhoneNumberValidator


class User(AbstractBaseUser, PermissionsMixin):
    phone = models.CharField(
        'номер телефона',
        unique=True,
        max_length=settings.PHONE_MAX_LENGTH,
        validators=[PhoneNumberValidator],
        error_messages={
            'unique': 'Телефонный номер занят',
        },
    )
    invitation_code = models.CharField(
        'код приглашения',
        max_length=settings.REFERRER_CODE_MAX_LENGTH,
        null=True,
    )
    referrer_code = models.CharField(
        'код приглашающего',
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
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'

    def get_full_name(self):
        return self.phone

    def get_short_name(self):
        return self.phone


class UserConfirmationCode(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        verbose_name='пользователь',
        related_name='user',
    )
    key = models.CharField(
        'значение кода',
        max_length=settings.CONFIRMATION_CODE_LENGTH,
        unique=True,
    )
    create_date = models.DateTimeField(
        'дата создания',
        null=False,
        auto_now_add=True,
    )

    class Meta:
        verbose_name = 'код подтверждения'
        verbose_name_plural = 'коды подтверждения'


class Referring(models.Model):
    referral = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=False,
        verbose_name='приглашенный пользователь',
        related_name='referral',
    )
    referrer = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=False,
        verbose_name='пригласивший пользователь',
        related_name='referrer',
    )

    class Meta:
        verbose_name = 'реферальная связь'
        verbose_name_plural = 'реферальные связи'
