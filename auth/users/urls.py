from django.urls import path
from .views import home, SignUp, ECSCreateView, ECSListView, profile
from .email_sender import CustomPasswordResetView

urlpatterns = [
 path('', home, name = "home"),
 path("signup/", SignUp.as_view(), name="signup"),

 path('create/', ECSCreateView.as_view(), name='ecs-create'),
 path('list/', ECSListView.as_view(), name='ecs-list'),
 path('profile/', profile, name='profile'),

 path('password_reset/', CustomPasswordResetView.as_view(), name='password_reset'),
]

