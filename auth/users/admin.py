from django.contrib import admin

# Register your models here.
from .models import ExtracurricularReference

@admin.register(ExtracurricularReference)
class ExtracurricularReferenceAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'website', 'field', 'type', 'mode', 'season', 'selectivity', 'cost']