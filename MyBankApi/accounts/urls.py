from django.urls import path, include
from accounts.views import UserRegistrationView, UserLoginView, UserLogoutView
from django.views.generic import TemplateView

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='user_registration'),
    path('login/', UserLoginView.as_view(), name='user_login'),
    path('logout/', UserLogoutView.as_view(), name='user_logout'),
]
