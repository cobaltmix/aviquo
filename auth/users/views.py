from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from django.template import loader
from .models import Extracurricular
from django.http import HttpResponse
# Create your views here.

def home(request):
    extracurriculars = Extracurricular.objects.all().values()
    template = loader.get_template('users/home.html')
    context = {
        'extracurriculars': extracurriculars,
    }
    return HttpResponse(template.render(context, request))



class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"