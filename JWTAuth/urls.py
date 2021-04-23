from django.conf.urls import url
from .views import RegisterView, EmployeeView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    url("login/", TokenObtainPairView.as_view(), name='token_obtain_pair'),
    url('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    url('register/', RegisterView.as_view(), name='auth_register'),
    url('user/', EmployeeView.as_view()),

]