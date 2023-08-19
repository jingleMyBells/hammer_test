from django.urls import path

from api_auth.views import ConfirmationCodeRequestView, TokenRequestView

app_name = 'api_auth'

urlpatterns = [
    path(
        'request_code/',
        ConfirmationCodeRequestView.as_view(),
        name='request_code',
    ),
    path('request_token/', TokenRequestView.as_view(), name='request_token'),
]
