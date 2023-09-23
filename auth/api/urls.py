# api_app/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, ECSViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'ecs', ECSViewSet)
urlpatterns = [
    path('', include(router.urls)),
]
