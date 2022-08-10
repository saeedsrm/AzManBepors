from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from accounts.views import RegisterView,UserUpdateView,UserDeleteView

urlpatterns = [

    path('register/', RegisterView.as_view(), name='auth_register'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('user-update/<int:pk>/', UserUpdateView.as_view(), name='user-update'),
    path('user-delete/<int:pk>/', UserDeleteView.as_view(), name='user-delete'),
]
