# api_app/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, ForumViewSet, UserRegistrationView, UserLoginView, OpportunityViewSet, TagViewSet, gen_api_key
from django.contrib.auth import get_user_model
User = get_user_model()

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'Forum', ForumViewSet)
router.register(r'Opportunity', OpportunityViewSet)
router.register(r'Tag', TagViewSet)
urlpatterns = [
    path('', include(router.urls)),
    path('gen_key/', gen_api_key, name = "GAK"),
    path('register/', UserRegistrationView.as_view(), name='user-registration'),
    path('login/', UserLoginView.as_view(), name='user-login'),
]
