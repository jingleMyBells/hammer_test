from django.contrib import admin
from django.urls import include, path

import api_referrals.urls

urlpatterns = [
    path('api/v1/', include(api_referrals.urls)),
]
