from django.db import models
from django.contrib.auth.models import User


class Doctor(models.Model):
    """
    The Doctor model represents a doctor in the hospital.

    Each doctor has a one-to-one relation with a User, which is used for authentication.
    Each doctor also has a description, a department, a photo, a phone number, and a NID.

    Attributes:
        user (OneToOneField): The user associated with the doctor.
        description (TextField): The description of the doctor.
        department (CharField): The department of the doctor.
        photo (ImageField): The photo of the doctor.
        phone_number (CharField): The phone number of the doctor.
        nid (CharField): The NID of the doctor.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    description = models.TextField()
    department = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='doctors/')
    phone_number = models.CharField(max_length=15)
    nid = models.CharField(max_length=20)

    def __str__(self):
        return self.user.username


class Timing(models.Model):
    """
    The Timing model represents a timing slot for a doctor.

    Each timing slot has a day, a time period, and is associated with a specific doctor.

    Attributes:
        day (CharField): The day of the timing slot.
        time_period (CharField): The time period of the timing slot.
        doctor (ForeignKey): The doctor associated with the timing slot.
    """
    day = models.CharField(max_length=20)
    time_period = models.CharField(max_length=50)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='timings')

    def __str__(self):
        return f"{self.day} {self.time_period}"


class Patient(models.Model):
    """
    The Patient model represents a patient in the hospital.

    Each patient has a one-to-one relation with a User, which is used for authentication.
    Each patient also has an age, a blood group, a photo, a phone number, and a NID.

    Attributes:
        user (OneToOneField): The user associated with the patient.
        age (IntegerField): The age of the patient.
        blood_group (CharField): The blood group of the patient.
        photo (ImageField): The photo of the patient.
        phone_number (CharField): The phone number of the patient.
        nid (CharField): The NID of the patient.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField()
    blood_group = models.CharField(max_length=3, blank=True)
    photo = models.ImageField(upload_to='patients/', blank=True)
    phone_number = models.CharField(max_length=15)
    nid = models.CharField(max_length=20)

    def __str__(self):
        return self.user.username


class Appointment(models.Model):
    """
    The Appointment model represents an appointment in the hospital.

    Each appointment is associated with a specific doctor and patient,
    and has a date and selected timing.

    Attributes:
        doctor (ForeignKey): The doctor associated with the appointment.
        patient (ForeignKey): The patient associated with the appointment.
        date (DateField): The date of the appointment.
        timing (ForeignKey): The selected timing of the appointment from the doctor's timings.
    """
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date = models.DateField()
    timing = models.ForeignKey(Timing, on_delete=models.CASCADE)

    def __str__(self):
        return f"Appointment: {self.doctor} - {self.patient} - {self.date} - {self.timing}"
