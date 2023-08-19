from http import HTTPStatus

import rest_framework.permissions
from django.contrib.auth import get_user_model
from rest_framework import mixins, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from api_referrals.serializers import UserSerializer, ReferrerCode
from referrals.services import check_referring, create_referring

User = get_user_model()


class UserViewSet(mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (rest_framework.permissions.IsAuthenticated,)

    @action(methods=['post'], detail=True)
    def add_referrer(self, request, pk):
        if request.user.pk != int(pk):
            return Response(
                'Редактировать чужие профили нельзя',
                HTTPStatus.FORBIDDEN,
            )
        existing_code = check_referring(request.user)
        if isinstance(existing_code, str):
            code_serializer = ReferrerCode(
                data={'referrer_code': existing_code},
            )
            code_serializer.is_valid(raise_exception=True)
            return Response(code_serializer.data, HTTPStatus.ALREADY_REPORTED)
        code_serializer = ReferrerCode(data=request.data)
        code_serializer.is_valid(raise_exception=True)
        is_success = create_referring(
            request.user,
            code_serializer.validated_data.get('referrer_code'),
        )
        if is_success:
            return Response(
                'Успешно добавлен пригласивший вас пользователь',
                HTTPStatus.CREATED,

            )
        return Response(
            'Не удалось добавить приглашение, обратитесь в техподдержку',
            HTTPStatus.IM_A_TEAPOT,
        )
