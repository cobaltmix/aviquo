# api_app/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet

router = DefaultRouter()
router.register(r'api', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
