from django.contrib import admin

# Register your models here.
from .models import ExtracurricularReference, AwardReference, ScholarshipReference

@admin.register(ExtracurricularReference)
class ExtracurricularReferenceAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'website', 'field', 'type', 'mode', 'season', 'selectivity', 'cost']

@admin.register(AwardReference)
class AwardReferenceAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'website', 'field', 'type', 'mode', 'season', 'selectivity', 'cost']

@admin.register(ScholarshipReference)
class ScholarshipReferenceAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'website', 'field', 'type', 'mode', 'season', 'selectivity', 'cost']