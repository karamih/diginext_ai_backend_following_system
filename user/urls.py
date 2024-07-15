from django.urls import path

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import RegisterUserView

urlpatterns = [
    path('user/login', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('user/register', RegisterUserView.as_view(), name='user-register'),
    path('user/refreshToken', TokenRefreshView.as_view(), name='token_refresh'),
]