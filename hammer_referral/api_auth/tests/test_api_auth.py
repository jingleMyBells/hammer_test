import pytest

from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient

User = get_user_model()


class TestApiAuth:

    def setup_class(self):
        self.request_code = reverse('api_auth:request_code')
        self.request_token = reverse('api_auth:request_token')
        self.new_phone = '79245739763'

    @pytest.mark.django_db(transaction=True)
    def test_add_new_user(self, client):

        user_exists = User.objects.filter(phone=self.new_phone).exists()

        assert user_exists is False, (
            'Тестовый юзер есть в базе в начале тестов',
        )

        data = {'phone': self.new_phone}
        response = client.post(self.request_code, data=data)

        assert response.status_code == 200, (
            'При попытке начать аутентификацию '
            'несуществующим юзером не возвращается статус 200'
        )

        response_data = response.json().get('code')

        assert isinstance(response_data, str), (
            'code содержит что-то неожиданное',
        )

        user_exists = User.objects.filter(
            phone=self.new_phone,
        ).exists()

        assert user_exists is True, (
            'Тестовый юзер не появился в базе после попытки создания',
        )

        user = User.objects.filter(phone=self.new_phone).first()

        token_exists = Token.objects.filter(user=user).exists()

        assert token_exists is False, (
            'Токен нового юзера существует до попытки аутентификации',
        )

        response = client.post(
            self.request_token,
            data={'code': response_data},
        )

        token_received = response.json().get('token')

        assert token_received == Token.objects.filter(user=user).first().key, (
            'Вовзращаемый api токен не совпадает со сгененренным для юзера'
        )

    @pytest.mark.django_db(transaction=True)
    def test_auth_existing_user(self, client, user):

        response = client.post(self.request_code, data={'phone': user.phone})

        assert response.status_code == 200, (
            'При попытке начать аутентификацию '
            'существующим юзером не возвращается статус 200'
        )

        response_data = response.json().get('code')

        assert isinstance(response_data, str), (
            'code содержит что-то неожиданное',
        )

        response = client.post(self.request_code, data={'code': response_data})

        response_data = response.json().get('token')

        auth_client = APIClient()
        auth_client.credentials(HTTP_AUTHORIZATION={f'Token {response_data}'})

        profile = f'/api/v1/user/{user.pk}'

        response = client.get(profile)

        assert response.status_code in (200, 301), (
            'Авторизованного юзера не пускает в профиль',
        )
