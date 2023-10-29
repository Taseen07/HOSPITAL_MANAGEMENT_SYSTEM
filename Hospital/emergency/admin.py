from django.contrib import admin
from .models import EmergencyService, EmergencyServiceRequest


class EmergencyServiceAdmin(admin.ModelAdmin):
    """
    Admin interface for the EmergencyService model.
    """
    list_display = ['service_type', 'cost', 'ETA']
    list_filter = ['service_type']
    search_fields = ['service_type']


admin.site.register(EmergencyService, EmergencyServiceAdmin)


class EmergencyServiceRequestAdmin(admin.ModelAdmin):
    """
    Admin interface for the EmergencyServiceRequest model.
    """
    list_display = ['patient', 'service', 'request_date', 'status']
    list_filter = ['status', 'request_date', 'service']
    search_fields = ['patient__username', 'service__service_type']
    list_editable = ['status']  # This makes 'status' editable directly from the list view


admin.site.register(EmergencyServiceRequest, EmergencyServiceRequestAdmin)
