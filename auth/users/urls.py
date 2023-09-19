from django.urls import path
from .views import home, SignUp, ECSCreateView, ECSListView

urlpatterns = [
 path('', home, name = "home"),
 path("signup/", SignUp.as_view(), name="signup"),

 path('create/', ECSCreateView.as_view(), name='ecs-create'),
 path('list/', ECSListView.as_view(), name='ecs-list'),
]