from django import forms
from .models import EmergencyServiceRequest, EmergencyService

# Define a form class for EmergencyServiceRequest
class EmergencyServiceRequestForm(forms.ModelForm):
    class Meta:
        # Associate the form with the EmergencyServiceRequest model
        model = EmergencyServiceRequest
        # Specify the fields to include in the form
        fields = ['service']

