from django.core.validators import RegexValidator


class PhoneNumberValidator(RegexValidator):
    regex = r'^((\+7|7|8)+([0-9]){10})$'
    message = 'Incorrect phone number'
