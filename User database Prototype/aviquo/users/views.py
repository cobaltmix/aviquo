from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import User
# Create your views here.

def users(request):
    myusers = User.objects.all().values()
    template = loader.get_template('all_users.html')
    context = {
        'myusers': myusers,
    }
    return HttpResponse(template.render(context, request))