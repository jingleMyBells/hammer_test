import re

from django.conf import settings
from rest_framework import serializers


class PhoneSerializer(serializers.Serializer):
    phone = serializers.CharField(required=True)

    def validate_phone(self, value):
        regex = r'^((\+7|7|8)+([0-9]){10})$'
        pattern = re.compile(regex)
        if not pattern.match(value):
            raise serializers.ValidationError('Incorrect phone number')
        return value


class ConfirmationCodeSerializer(serializers.Serializer):
    code = serializers.CharField(
        min_length=settings.CONFIRMATION_CODE_LENGTH,
        max_length=settings.CONFIRMATION_CODE_LENGTH,
    )


class TokenSerializer(serializers.Serializer):
    token = serializers.CharField()