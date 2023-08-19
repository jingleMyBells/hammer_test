import random
import string

from django.conf import settings
from django.contrib.auth.base_user import BaseUserManager


def generate_referrer_code(length):
    symbols = string.ascii_lowercase + string.digits
    return ''.join(random.sample(symbols, length))


class CustomUserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, phone, password, **extra_fields):
        while True:
            code = generate_referrer_code(settings.REFERRER_CODE_MAX_LENGTH)
            if not self.model.objects.filter(referrer_code=code).exists():
                break
        user = self.model(phone=phone, referrer_code=code, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, phone, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(phone, password, **extra_fields)

    def create_superuser(self, phone, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(phone, password, **extra_fields)
