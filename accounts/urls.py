"""
URL Patterns for accounts/ route.
Dec 19, 2021
@narender

"""
from django.urls import path, include 
from django.contrib.auth.views import (
    LoginView,
    LogoutView
)
from accounts.views import registerView, logoutView

urlpatterns = [
    path('register/', registerView , name='register'),
    path('login/', LoginView.as_view(template_name = 'accounts/login.html'),name='login'),
    path('logout/', logoutView ,name='logout'),
]