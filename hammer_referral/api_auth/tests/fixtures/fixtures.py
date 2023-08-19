import pytest
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient

User = get_user_model()


@pytest.fixture
def api_auth_user_1():
    return User.objects.create(phone='+79265639973')


@pytest.fixture
def api_auth_user_1():
    return User.objects.create(phone='89366710951')
