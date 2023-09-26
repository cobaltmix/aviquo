from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from .models import ExtracurricularReference, AwardReference, ScholarshipReference, Forum
from rest_framework import generics
from .serializers import ECSSerializer, AWSSerializer, SCSerializer, ForumSerializer
from django import forms
from django.shortcuts import render, redirect

from django.contrib.auth import get_user_model
User = get_user_model()

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



class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)  # Make the email field required

    class Meta:
        model = User
        fields = UserCreationForm.Meta.fields + ('email',)

class SignUp(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

class ForumView(generics.CreateAPIView):
    queryset = Forum.objects.all()
    serializer_class = ForumSerializer

class ECSCreateView(generics.CreateAPIView):
    queryset = ExtracurricularReference.objects.all()
    serializer_class = ECSSerializer

class ECSListView(generics.ListAPIView):
    queryset = ExtracurricularReference.objects.all()
    serializer_class = ECSSerializer

class AWSCreateView(generics.CreateAPIView):
    queryset = AwardReference.objects.all()
    serializer_class = AWSSerializer

class AWSListView(generics.ListAPIView):
    queryset = AwardReference.objects.all()
    serializer_class = AWSSerializer

class SCCreateView(generics.CreateAPIView):
    queryset = ScholarshipReference.objects.all()
    serializer_class = SCSerializer

class SCCListView(generics.ListAPIView):
    queryset = ScholarshipReference.objects.all()
    serializer_class = SCSerializer
