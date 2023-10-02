# api_app/urls.py
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (
    ForumViewSet,
    OpportunityViewSet,
    RegistrationAPIView,
    TagViewSet,
    UserViewSet,
    WaitlistViewSet,
    gen_api_key,
)

router = DefaultRouter()
router.register(r"users", UserViewSet)
router.register(r"Forum", ForumViewSet)
router.register(r"Opportunity", OpportunityViewSet)
router.register(r"Tag", TagViewSet)
router.register(r"Waitlist", WaitlistViewSet)
urlpatterns = [
    path("", include(router.urls)),
    path("gen_key/", gen_api_key, name="GAK"),
    path("register/", RegistrationAPIView.as_view(), name="register"),
    # path('login/', LoginAPIView.as_view(), name='token_obtain_pair'),
    # path('token-refresh/', TokenRefreshAPIView.as_view(), name='token_refresh'),
]
