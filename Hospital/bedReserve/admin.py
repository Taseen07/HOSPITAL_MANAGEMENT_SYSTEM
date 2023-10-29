from django.contrib import admin
from .models import HospitalBeds

@admin.register(HospitalBeds)
class HospitalBedsAdmin(admin.ModelAdmin):
    """
    Admin view configuration for HospitalBeds model.
    """
    list_display = ('category', 'position', 'rent_per_day', 'is_available')
    list_filter = ('category', 'is_available')
    search_fields = ('position', 'category')
    actions = ['make_available', 'make_unavailable']

    def make_available(self, request, queryset):
        """
        Action to mark selected beds as available.

        Args:
            request: HttpRequest object.
            queryset: Selected beds queryset.

        Returns:
            None
        """
        queryset.update(is_available=True)

    make_available.short_description = "Mark selected beds as available"

    def make_unavailable(self, request, queryset):
        """
        Action to mark selected beds as unavailable.

        Args:
            request: HttpRequest object.
            queryset: Selected beds queryset.

        Returns:
            None
        """
        queryset.update(is_available=False)

    make_unavailable.short_description = "Mark selected beds as unavailable"






