from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from .models import ExtracurricularReference
from rest_framework import generics
from .serializers import ECSSerializer
# Create your views here.

def home(request):
    return render(request, 'users/home.html', {})

def profile(request):
    return render(request, 'users/profile.html', {})

class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

class ECSCreateView(generics.CreateAPIView):
    queryset = ExtracurricularReference.objects.all()
    serializer_class = ECSSerializer

class ECSListView(generics.ListAPIView):
    queryset = ExtracurricularReference.objects.all()
    serializer_class = ECSSerializer