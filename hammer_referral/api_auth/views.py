from http import HTTPStatus
import time

from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.views import APIView

from api_auth.exceptions import InvalidConfirmationCode, PhoneNotFound
from api_auth.serializers import ConfirmationCodeSerializer, PhoneSerializer, TokenSerializer
from api_auth.services import generate_token, get_user_by_code, get_user_by_phone, create_user_confirmation_code

User = get_user_model()


class ConfirmationCodeRequestView(APIView):
    def post(self, request):
        phone_serializer = PhoneSerializer(data=request.data)
        phone_serializer.is_valid(raise_exception=True)
        try:
            user = get_user_by_phone(
                phone_serializer.validated_data.get('phone'),
            )
            code = create_user_confirmation_code(user)
            print(code)
            code_serializer = ConfirmationCodeSerializer(
                data={'code': code},
            )
            code_serializer.is_valid(raise_exception=True)
            time.sleep(2)  # имитация задержки на отсылку кода
            return Response(code_serializer.data)
        except PhoneNotFound as e:
            return Response(e.args, HTTPStatus.NOT_FOUND)


class TokenRequestView(APIView):
    def post(self, request):
        """Тут надо создать для юзера токен и вернуть ему"""
        code_serializer = ConfirmationCodeSerializer(data=request.data)
        code_serializer.is_valid(raise_exception=True)
        try:
            user = get_user_by_code(code_serializer.validated_data.get('code'))
            token, created = generate_token(user)
            token_serializer = TokenSerializer(data={'token': token.key})
            token_serializer.is_valid(raise_exception=True)
            return Response(token_serializer.data)
        except InvalidConfirmationCode as e:
            return Response(e.args, HTTPStatus.NOT_FOUND)

