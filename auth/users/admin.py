from django.contrib import admin
from .models import Opportunity, Forum
from django.contrib.auth import get_user_model
User = get_user_model()

# Define custom admin classes for each model

# Register your models with the custom admin classes
admin.site.register(Opportunity)
admin.site.register(Forum)
