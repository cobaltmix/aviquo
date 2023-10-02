from django.contrib import admin
from .models import Opportunity, Forum, Tag, Waitlist, CustomUser

from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User


# Define custom admin classes for each model
class CustomUserInline(admin.StackedInline):
    model = CustomUser
    can_delete = False
    verbose_name_plural = "user"

class CustomUserAdmin(BaseUserAdmin):
    inlines = [CustomUserInline]

# Register your models with the custom admin classes
admin.site.register(Opportunity)
admin.site.register(Forum)
admin.site.register(Tag)
admin.site.register(Waitlist)

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)