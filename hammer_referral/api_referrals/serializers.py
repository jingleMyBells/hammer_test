from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    invited_users = serializers.SerializerMethodField(method_name='get_referrals')

    class Meta:
        model = User
        fields = ('phone', 'invited_users')

    def get_referrals(self, obj):
        code = obj.referrer_code
        result = []
        for user in User.objects.filter(invitation_code=code):
            result.append(user.phone)
        return result
