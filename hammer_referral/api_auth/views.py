from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView

from api_auth.serializers import ConfirmationCodeSerializer, PhoneSerializer, TokenSerializer

User = get_user_model()


class ConfirmationCodeRequestView(APIView):
    def post(self, request):
        """Тут надо принять телефон, если юезра нет - создать, если юзер есть - выслать код"""
        serializer = PhoneSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        print(serializer.is_valid(raise_exception=True))
        print(serializer.validated_data.get('phone'))
        return Response('lalala')


class TokenRequestView(APIView):
    def post(self, request):
        """Тут надо создать для юзера токен и вернуть ему"""
        user = User.objects.first()
        token = Token.objects.create(user=user)
        return Response(token)

