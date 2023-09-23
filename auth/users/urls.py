from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import home, SignUp, profile
from .email_sender import CustomPasswordResetView
from django.urls import path, include


urlpatterns = [
 path('', home, name = "home"),
 path("signup/", SignUp.as_view(), name="signup"),

 path('profile/', profile, name='profile'),

 path('password_reset/', CustomPasswordResetView.as_view(), name='password_reset'),
]

