from django.urls import include, path

import api_referrals.urls
import api_auth.urls

urlpatterns = [
    path('api/v1/auth/', include(api_auth.urls)),
    path('api/v1/', include(api_referrals.urls)),
]
