import rest_framework.permissions
from django.contrib.auth import get_user_model
from rest_framework import mixins, viewsets

from api_referrals.serializers import UserSerializer

User = get_user_model()


class UserViewSet(mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (rest_framework.permissions.IsAuthenticated,)
