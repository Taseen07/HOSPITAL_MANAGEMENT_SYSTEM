from django.contrib import admin
from .models import DiagnosticCategory, DiagnosticTest


@admin.register(DiagnosticCategory)
class DiagnosticCategoryAdmin(admin.ModelAdmin):
    """Admin interface for the DiagnosticCategory model."""

    list_display = ['name']


@admin.register(DiagnosticTest)
class DiagnosticTestAdmin(admin.ModelAdmin):
    """Admin interface for the DiagnosticTest model."""

    list_display = ['name', 'description', 'duration', 'cost', 'category']
    list_filter = ['category']
    search_fields = ['name', 'category__name']
