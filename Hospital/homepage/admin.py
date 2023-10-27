# admin.py
from django.contrib import admin
from .models import Doctor, Patient, Appointment

# Admin interface for Doctor model
class DoctorAdmin(admin.ModelAdmin):
    pass

# Admin interface for Patient model
class PatientAdmin(admin.ModelAdmin):
    pass

# Admin interface for Appointment model
class AppointmentAdmin(admin.ModelAdmin):
    pass

# Register Doctor model with custom DoctorAdmin interface
admin.site.register(Doctor, DoctorAdmin)

# Register Patient model with custom PatientAdmin interface
admin.site.register(Patient, PatientAdmin)

# Register Appointment model with custom AppointmentAdmin interface
admin.site.register(Appointment, AppointmentAdmin)
