from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from .models import ExtracurricularReference, AwardReference, ScholarshipReference
from rest_framework import generics
from .serializers import ECSSerializer, AWSSerializer, SCSerializer, UserSerializer
from django import forms
from django.shortcuts import render, redirect
from rest_framework import viewsets


# Create your views here.
class EditProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']


def home(request):
    return render(request, 'users/home.html', {})


@login_required
def profile(request):
    user = request.user

    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('profile')

    else:
        form = EditProfileForm(instance=user)

    return render(request, 'users/profile.html', {'user': user, 'form': form})


class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


# class ECSCreateView(generics.CreateAPIView):
#     queryset = ExtracurricularReference.objects.all()
#     serializer_class = ECSSerializer


class ECSListView(viewsets.ModelViewSet):
    queryset = ExtracurricularReference.objects.all()
    serializer_class = ECSSerializer

    def get_queryset(self):
        # aggregate query params
        filter_params = {key: self.request.query_params.get(key) for key in
                         [field.name for field in ExtracurricularReference._meta.get_fields()]}

        # eliminate nonexistent params & filter from model
        return ExtracurricularReference.objects.filter(**{k: v for k, v in filter_params.items() if v is not None})


# class AWSCreateView(generics.CreateAPIView):
#     queryset = AwardReference.objects.all()
#     serializer_class = AWSSerializer


class AWSListView(viewsets.ModelViewSet):
    queryset = AwardReference.objects.all()
    serializer_class = AWSSerializer

    def get_queryset(self):
        # aggregate query params
        filter_params = {key: self.request.query_params.get(key) for key in
                         [field.name for field in AwardReference._meta.get_fields()]}

        # eliminate nonexistent params & filter from model
        return AwardReference.objects.filter(**{k: v for k, v in filter_params.items() if v is not None})


# class SCCreateView(generics.CreateAPIView):
#     queryset = ScholarshipReference.objects.all()
#     serializer_class = SCSerializer


class SCCListView(viewsets.ModelViewSet):
    queryset = ScholarshipReference.objects.all()
    serializer_class = SCSerializer

    def get_queryset(self):
        # aggregate query params
        filter_params = {key: self.request.query_params.get(key) for key in
                         [field.name for field in ScholarshipReference._meta.get_fields()]}

        # eliminate nonexistent params & filter from model
        return ScholarshipReference.objects.filter(**{k: v for k, v in filter_params.items() if v is not None})


class UsersListView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_queryset(self):
        # aggregate query params
        filter_params = {key: self.request.query_params.get(key) for key in
                         [field.name for field in User._meta.get_fields()]}

        # eliminate nonexistent params & filter from model
        return User.objects.filter(**{k: v for k, v in filter_params.items() if v is not None})
