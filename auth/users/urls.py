from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import home, SignUp, ECSListView, profile, AWSListView, SCCListView, UsersListView
from .email_sender import CustomPasswordResetView
from django.urls import path, include

router = DefaultRouter()
router.register(r'users', UsersListView)
router.register(r'ECS', ECSListView)
router.register(r'AWS', AWSListView)
router.register(r'SC', SCCListView)
urlpatterns = [
 path('', include(router.urls)),
 path('', home, name = "home"),
 path("signup/", SignUp.as_view(), name="signup"),
 # path('ec/create/', ECSCreateView.as_view(), name='ecs-create'),
 # path('ec/list/', ECSListView.as_view(), name='ecs-list'),
 # path('aws/create/', AWSCreateView.as_view(), name='aws-create'),
 # path('aws/list/', AWSListView.as_view(), name='aws-list'),
 # path('sc/create/', SCCreateView.as_view(), name='sc-create'),
 # path('sc/list/', SCCListView.as_view(), name='sc-list'),
 path('profile/', profile, name='profile'),

 path('password_reset/', CustomPasswordResetView.as_view(), name='password_reset'),
]

