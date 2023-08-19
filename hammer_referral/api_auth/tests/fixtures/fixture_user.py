import pytest


@pytest.fixture
def user(django_user_model):
    return django_user_model.objects.create_user(
        phone='+78791231123',
    )
