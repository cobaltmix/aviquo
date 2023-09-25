# api_app/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, ECSViewSet, AWSViewSet, SCViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'ECS', ECSViewSet)
router.register(r'AWS', AWSViewSet)
router.register(r'SC', SCViewSet)
urlpatterns = [
    path('', include(router.urls)),
]
