import pytest

from django.contrib.auth import get_user_model

from referrals.models import Referring

User = get_user_model()


class TestApiReferrals:

    @pytest.mark.django_db(transaction=True)
    def test_user_profile(self, client, user_client, user_1):
        url = f'/api/v1/user/{user_1.pk}/'

        response = client.get(url)

        assert response.status_code == 401, (
            'Не авторизованного пустило в профиль',
        )

        response = user_client.get(url)

        assert response.status_code == 200, (
            'Авторизованного не пустило в профиль',
        )

        data = response.json()

        assert data.get('phone') == user_1.phone, (
            'Телефон из профиля не совпал с бд',
        )
        assert data.get('invitation_code',) == user_1.invitation_code, (
            'Код пригласившего из профиля не совпал с бд',
        )
        assert data.get('referrer_code') == user_1.referrer_code, (
            'Код для приглашения из профиля не совпал с бд',
        )

    def test_become_referral(self, user_client, user_1, user_2):

        referring_exists = Referring.objects.filter(
            referrer=user_2,
            referral=user_1,
        ).exists()

        assert referring_exists is False, (
            'Реферальное отношение существует до теста',
        )

        url = f'/api/v1/user/{user_1.pk}/'

        user_client.post(
            url + 'add_referrer/',
            data={'referrer_code': user_2.referrer_code},
        )
        response = user_client.get(url)

        response_data = response.json()

        referring_exists = Referring.objects.filter(
            referrer=user_2,
            referral=user_1,
        ).exists()

        assert referring_exists is True, (
            'Реферальное отношение не существует после приглашения',
        )
        assert response_data.get('invitation_code') == user_2.referrer_code, (
            'В профиле не появился код пригласившего',
        )
