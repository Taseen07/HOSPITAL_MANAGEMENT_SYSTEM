# models.py
from django.db import models
from django.contrib.auth.models import User


class Doctor(models.Model):
    """
    Doctor model with a one-to-one relation with User.
    Each doctor has a user associated with it.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    description = models.TextField()
    department = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='doctors/')
    phone_number = models.CharField(max_length=15)
    nid = models.CharField(max_length=20)


class Timing(models.Model):
    """
    Timing model for storing the day and time period.
    """
    day = models.CharField(max_length=20)
    time_period = models.CharField(max_length=50)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='timings')

    def __str__(self):
        return f"{self.day} {self.time_period}"


class Patient(models.Model):
    """
    Patient model with a one-to-one relation with User.
    Each patient has a user associated with it.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField()
    blood_group = models.CharField(max_length=3, blank=True)
    photo = models.ImageField(upload_to='patients/', blank=True)
    phone_number = models.CharField(max_length=15)
    nid = models.CharField(max_length=20)


class Appointment(models.Model):
    """
    Appointment model with foreign keys to Doctor and Patient.
    Each appointment is associated with a specific doctor and patient.
    """
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
