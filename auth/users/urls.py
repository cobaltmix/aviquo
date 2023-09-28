from django.urls import path
from .views import home, SignUp, OpportunityView, profile, ForumView, WaitlistView
from .email_sender import CustomPasswordResetView
from django.contrib.auth import get_user_model
User = get_user_model()
urlpatterns = [
 path('', home, name = "home"),
 path("signup/", SignUp.as_view(), name="signup"),

 path('opportunity/', OpportunityView.as_view(), name='opportunity'),
 path('waitlist /', WaitlistView.as_view(), name='waitlist'),
 path('forum/', ForumView.as_view(), name='forum'),
 path('profile/', profile, name='profile'),
 

 path('password_reset/', CustomPasswordResetView.as_view(), name='password_reset'),
]
