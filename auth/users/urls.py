from django.urls import path
from .views import home, SignUp, ECSCreateView, ECSListView, profile, AWSCreateView, AWSListView, SCCreateView, SCCListView, ForumView
from .email_sender import CustomPasswordResetView
from django.contrib.auth import get_user_model
User = get_user_model()
urlpatterns = [
 path('', home, name = "home"),
 path("signup/", SignUp.as_view(), name="signup"),

 path('ec/create/', ECSCreateView.as_view(), name='ecs-create'),
 path('ec/list/', ECSListView.as_view(), name='ecs-list'),
 path('aws/create/', AWSCreateView.as_view(), name='aws-create'),
 path('aws/list/', ECSListView.as_view(), name='aws-list'),
 path('sc/create/', AWSCreateView.as_view(), name='sc-create'),
 path('sc/list/', SCCListView.as_view(), name='sc-list'),
 path('forum/', ForumView.as_view(), name='forum'),
 path('profile/', profile, name='profile'),

 path('password_reset/', CustomPasswordResetView.as_view(), name='password_reset'),
]
