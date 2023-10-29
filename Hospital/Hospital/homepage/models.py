from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

# User model with basic information
class User(AbstractUser):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField()
    phone_number = models.CharField(max_length=15)
    gender = models.CharField(max_length=10)


# Doctor model extending User with additional information
class Doctor(User):
    department = models.CharField(max_length=100)
    qualification = models.CharField(max_length=200)
    email = models.EmailField(max_length=100)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, null=True)
    nid = models.CharField(max_length=20)
    is_approved = models.BooleanField(default=False)


# Patient model extending User with additional information
class Patient(User):
    blood_group = models.CharField(max_length=3, blank=True, null=True)
    nid = models.CharField(max_length=20)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, null=True)
