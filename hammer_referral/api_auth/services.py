from datetime import datetime, timezone

from django.conf import settings
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

from api_auth.exceptions import PhoneNotFound, InvalidConfirmationCode
from referrals.models import UserConfirmationCode
from referrals.services import generate_referrer_code


User = get_user_model()


def get_user_by_phone(phone):
    if User.objects.filter(phone=phone).exists():
        return User.objects.filter(phone=phone).first()
    raise PhoneNotFound('Не найден телефон')


def create_user_confirmation_code(user):
    while True:
        code = generate_referrer_code(settings.CONFIRMATION_CODE_LENGTH)
        if not UserConfirmationCode.objects.filter(key=code).exists():
            break
    UserConfirmationCode.objects.create(user=user, key=code)
    return code


def get_user_by_code(code):
    if not UserConfirmationCode.objects.filter(key=code).exists():
        raise InvalidConfirmationCode('Неверный код подтверждения')
    user_code = UserConfirmationCode.objects.select_related('user').filter(key=code).first()
    time_passed = datetime.now(timezone.utc) - user_code.create_date
    if time_passed.seconds > settings.CONFIRMATION_CODE_LIFETIME:
        raise InvalidConfirmationCode('Неверный код подтверждения')
    return user_code.user


def generate_token(user):
    return Token.objects.get_or_create(user=user)



