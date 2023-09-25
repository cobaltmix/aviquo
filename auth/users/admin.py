from django.contrib import admin
from .models import ExtracurricularReference, ScholarshipReference, AwardReference, Category

# Define custom admin classes for each model
class ExtracurricularReferenceAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'category', 'description', 'website', 'field', 'type', 'mode', 'season', 'selectivity', 'cost',
        'grade', 'location', 'offered_by', 'offered_by'
    )
    list_filter = (
        'category', 'field', 'type', 'mode', 'season', 'selectivity', 'cost',
        'grade', 'location', 'offered_by'
    )
    search_fields = ('name', 'description', 'website')

class ScholarshipReferenceAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'category', 'description', 'website', 'field', 'type', 'mode', 'season', 'selectivity', 'cost',
        'grade', 'location', 'offered_by', 'offered_by'
    )
    list_filter = (
        'category', 'field', 'type', 'mode', 'season', 'selectivity', 'cost',
        'grade', 'location', 'offered_by'
    )
    search_fields = ('name', 'description', 'website')

class AwardReferenceAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'category', 'description', 'website', 'field', 'type', 'mode', 'season', 'selectivity', 'cost',
        'grade', 'location', 'offered_by', 'offered_by'
    )
    list_filter = (
        'category', 'field', 'type', 'mode', 'season', 'selectivity', 'cost',
        'grade', 'location', 'offered_by'
    )
    search_fields = ('name', 'description', 'website')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

# Register your models with the custom admin classes
admin.site.register(ExtracurricularReference, ExtracurricularReferenceAdmin)
admin.site.register(ScholarshipReference, ScholarshipReferenceAdmin)
admin.site.register(AwardReference, AwardReferenceAdmin)
admin.site
