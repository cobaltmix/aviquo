# api_app/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, ECSListView, AWSListView, SCCListView

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'ECS', ECSListView)
router.register(r'AWS', AWSListView)
router.register(r'SC', SCCListView)
urlpatterns = [
    path('', include(router.urls)),
]
