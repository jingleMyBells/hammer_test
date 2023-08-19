from drf_spectacular.extensions import OpenApiViewExtension
from drf_spectacular.utils import (
    extend_schema,
    OpenApiExample,
    OpenApiResponse,
)


class UserView(OpenApiViewExtension):
    target_class = 'api_referrals.views.UserViewSet'

    def view_replacement(self):
        from api_referrals.serializers import UserSerializer, ReferrerCode

        class Extended(self.target_class):

            @extend_schema(
                description='Профиль пользователя',
                tags=['User'],
                responses={
                    200: OpenApiResponse(
                        response=UserSerializer,
                        examples=[
                            OpenApiExample(
                                '200',
                                summary='Валидный ответ',
                                description='Возвращает профиль',
                                value={
                                    'phone': '+75624567890',
                                    'invitation_code': (
                                            'какой-то код с '
                                            'которым юзера пригласили'
                                    ),
                                    'referrer_code': (
                                            'с этим кодом юзер '
                                            'сам кого-то пригласит'
                                    ),
                                    'invited_users': [
                                        '89234567890',
                                        '71234567890',
                                    ]
                                },
                            ),
                        ],
                    ),
                },
            )
            def retrieve(self):
                pass

            @extend_schema(
                description='Стать рефералом',
                tags=['User'],
                request=ReferrerCode,
                responses={
                    200: OpenApiResponse(
                        response=ReferrerCode,
                        examples=[
                            OpenApiExample(
                                '200',
                                summary='Валидный ответ',
                                description=(
                                        'Возвращает сообщение '
                                        'о результате'
                                ),
                                value=(
                                        'Успешно добавлен '
                                        'пригласивший вас пользователь',
                                ),
                            ),
                        ],
                    ),
                },
            )
            def add_referrer(self):
                pass

        return Extended
