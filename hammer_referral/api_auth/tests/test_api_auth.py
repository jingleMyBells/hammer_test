import pytest

from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()


class TestApiAuth:
    def setup_class(self):
        self.request_code = reverse('api_auth:request_code')
        self.request_token = reverse('api_auth:request_token')

    # def test_add_new_user
