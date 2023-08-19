from django.contrib.auth import get_user_model
from rest_framework import serializers

from referrals.models import Referring

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    invited_users = serializers.SerializerMethodField(
        method_name='get_referrals',
    )

    class Meta:
        model = User
        fields = ('phone', 'invitation_code', 'referrer_code', 'invited_users')

    def get_referrals(self, obj):
        result = []
        for referring in Referring.objects.select_related(
                'referral',
        ).filter(referrer=obj):
            result.append(referring.referral.phone)
        return result


class ReferrerCode(serializers.Serializer):
    referrer_code = serializers.CharField()
