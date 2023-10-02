"""
URL configuration for auth project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:wdwf
Function viewsee
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
<<<<<<< HEAD:backend/auth/urls.py
from django.urls import path,include
# from django.contrib.auth import get_user_model
# User = get_user_model()
=======
from django.urls import path, include
>>>>>>> 36f805169e405883de6a3ee8e8612efb2ae3b20c:backend/core/urls.py

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
    path("", include("main.urls")),
    path("api/", include("api.urls")),
]
