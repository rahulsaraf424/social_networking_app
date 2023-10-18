from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .views import UserLoginView, UserLogoutView, UserSignupView, UserSearchView

urlpatterns = [
    path('api/login/', UserLoginView.as_view(), name='user_login'),
    path('api/logout/', UserLogoutView.as_view(), name='user_logout'),
    path('api/signup/', UserSignupView.as_view(), name='user_signup'),
    path('api/search/', UserSearchView.as_view(), name='user_search'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
