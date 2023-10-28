#admin.py
# Importing required modules from Django
from django.contrib import admin

# Importing the models from the current directory
from .models import Doctor, Patient, Appointment


class DoctorAdmin(admin.ModelAdmin):
    """
    This class represents the admin interface for the Doctor model.
    Currently, it doesn't add any additional functionality to the default admin interface.
    """
    pass


class PatientAdmin(admin.ModelAdmin):
    """
    This class represents the admin interface for the Patient model.
    Currently, it doesn't add any additional functionality to the default admin interface.
    """
    pass


class AppointmentAdmin(admin.ModelAdmin):
    """
    This class represents the admin interface for the Appointment model.
    Currently, it doesn't add any additional functionality to the default admin interface.
    """
    pass


# Registering the Doctor model with the custom DoctorAdmin interface
admin.site.register(Doctor, DoctorAdmin)

# Registering the Patient model with the custom PatientAdmin interface
admin.site.register(Patient, PatientAdmin)

# Registering the Appointment model with the custom AppointmentAdmin interface
admin.site.register(Appointment, AppointmentAdmin)
