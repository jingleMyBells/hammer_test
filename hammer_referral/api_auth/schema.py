from drf_spectacular.extensions import OpenApiViewExtension
from drf_spectacular.utils import (
    extend_schema,
    OpenApiExample,
    OpenApiResponse,
)


class ConfirmationCodeView(OpenApiViewExtension):
    target_class = 'api_auth.views.ConfirmationCodeRequestView'

    def view_replacement(self):
        from api_auth.serializers import (
            ConfirmationCodeSerializer,
            PhoneSerializer,
        )

        class Extended(self.target_class):

            @extend_schema(
                description='Получение кода аутентификации по телефону',
                tags=['Auth'],
                request=PhoneSerializer,
                responses={
                    200: OpenApiResponse(
                        response=ConfirmationCodeSerializer,
                        examples=[
                            OpenApiExample(
                                '200',
                                summary='Валидный ответ',
                                description='Возвращает код',
                                value={
                                    'code': 'dfg3',
                                },
                            ),
                        ],
                    ),
                },
            )
            def post(self):
                pass

        return Extended


class TokenView(OpenApiViewExtension):
    target_class = 'api_auth.views.TokenRequestView'

    def view_replacement(self):
        from api_auth.serializers import (
            ConfirmationCodeSerializer,
            TokenSerializer,
        )

        class Extended(self.target_class):

            @extend_schema(
                description='Получение токена аутентификации',
                tags=['Auth'],
                request=ConfirmationCodeSerializer,
                responses={
                    200: OpenApiResponse(
                        response=TokenSerializer,
                        examples=[
                            OpenApiExample(
                                '200',
                                summary='Валидный ответ',
                                description='Возвращает токен',
                                value={
                                    'token': '5465rthgfbvwert49h8gf7sd',
                                },
                            ),
                        ],
                    ),
                },
            )
            def post(self):
                pass

        return Extended
