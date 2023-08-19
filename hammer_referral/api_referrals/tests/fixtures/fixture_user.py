import pytest

from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token


@pytest.fixture
def user_1(django_user_model):
    return django_user_model.objects.create_user(
        phone='+78791231122',
    )


@pytest.fixture
def user_2(django_user_model):
    return django_user_model.objects.create_user(
        phone='+79045677891',
    )


@pytest.fixture
def user_token(user_1):
    token, create = Token.objects.get_or_create(user=user_1)
    return token


@pytest.fixture
def user_client(user_token):
    client = APIClient()
    token = user_token
    client.credentials(HTTP_AUTHORIZATION=f'Token {token.key}')
    return client
