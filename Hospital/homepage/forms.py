# forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Doctor, Patient, Timing


class UserRegistrationForm(UserCreationForm):
    """
    Form for registering a new user.
    """

    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ('first_name', 'last_name',)


class TimingForm(forms.ModelForm):
    """
    Form for creating a new timing.
    """

    class Meta:
        model = Timing
        fields = ['day', 'time_period']


class DoctorForm(forms.ModelForm):
    """
    Form for registering a new doctor.
    """

    class Meta:
        model = Doctor
        fields = ['description', 'department', 'photo', 'phone_number', 'nid']


class PatientForm(forms.ModelForm):
    """
    Form for registering a new patient.
    """

    class Meta:
        model = Patient
        fields = ['age', 'blood_group', 'photo', 'phone_number', 'nid']

class DoctorSearchForm(forms.Form):
    """
       Form for searching doctor.
       """
    search_term = forms.CharField(max_length=200)