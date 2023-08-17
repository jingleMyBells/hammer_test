from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api_referrals.views import UserViewSet

app_name = 'api_referrals'

router_v1_user = DefaultRouter()

router_v1_user.register(r'user', UserViewSet, basename='user')

urlpatterns = [
    path('', include(router_v1_user.urls)),
]
