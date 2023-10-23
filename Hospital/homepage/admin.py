from django.contrib import admin
from .models import Doctor, User, Patient
# Register your models here.
class DoctorAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        # Set approved as False when first created.
        if getattr(obj, 'approved', None) is None:
            obj.approved = False
        obj.save()

admin.site.register(User)
admin.site.register(Patient)
admin.site.register(Doctor, DoctorAdmin)


