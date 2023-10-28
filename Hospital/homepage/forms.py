from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Doctor, Patient, Timing, Appointment


class UserRegistrationForm(UserCreationForm):
    """
    A form for registering a new user.

    This form inherits from UserCreationForm and adds fields for the first name
    and last name of the user.

    Attributes:
        Meta.fields (tuple): A tuple containing the fields of UserCreationForm
                             plus 'first_name' and 'last_name'.
    """

    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ('first_name', 'last_name',)


class TimingForm(forms.ModelForm):
    """
    A form for creating a new timing.

    This form is a ModelForm for the Timing model. It includes fields for the day
    and time period of the timing.

    Attributes:
        Meta.model (Model): The model class this form is associated with (Timing).
        Meta.fields (list): The fields included in this form.
    """

    class Meta:
        model = Timing
        fields = ['day', 'time_period']


class DoctorForm(forms.ModelForm):
    """
    A form for registering a new doctor.

    This form is a ModelForm for the Doctor model. It includes fields for the description,
    department, photo, phone number, and NID of the doctor.

    Attributes:
        Meta.model (Model): The model class this form is associated with (Doctor).
        Meta.fields (list): The fields included in this form.
    """

    class Meta:
        model = Doctor
        fields = ['description', 'department', 'photo', 'phone_number', 'nid']


class PatientForm(forms.ModelForm):
    """
    A form for registering a new patient.

    This form is a ModelForm for the Patient model. It includes fields for the age,
    blood group, photo, phone number, and NID of the patient.

    Attributes:
        Meta.model (Model): The model class this form is associated with (Patient).
        Meta.fields (list): The fields included in this form.
    """

    class Meta:
        model = Patient
        fields = ['age', 'blood_group', 'photo', 'phone_number', 'nid']


class DoctorSearchForm(forms.Form):
    """
       A form for searching doctors.

       This form includes a single field for the search term.

       Attributes:
           search_term (CharField): The field for the search term.
       """

    search_term = forms.CharField(max_length=200)

class AppointmentForm(forms.ModelForm):
    """
    A form for booking a doctor appointment.

    This form is associated with the Appointment model. It includes fields for selecting
    a timing.

    Attributes:
        timing (ModelChoiceField): A field for selecting a timing.
    """
    timing = forms.ModelChoiceField(queryset=Timing.objects.none())

    class Meta:
        model = Appointment
        fields = ['timing']
