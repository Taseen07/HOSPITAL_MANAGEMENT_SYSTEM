from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

# Create your models here.

# User model with basic information
class User(AbstractUser):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField()
    phone_number = models.CharField(max_length=15)
    gender = models.CharField(max_length=10)

    # Add related_name argument to groups field
    groups = models.ManyToManyField(Group, related_name='custom_user_set')
    user_permissions = models.ManyToManyField(Permission, related_name='custom_user_set')


# Doctor model extending User with additional information
class Doctor(User):
    department = models.CharField(max_length=100)
    qualification = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, null=True)
    nid = models.CharField(max_length=20)
    is_approved = models.BooleanField(default=False)


# Patient model extending User with additional information
class Patient(User):
    blood_group = models.CharField(max_length=3, blank=True, null=True)
    nid = models.CharField(max_length=20)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, null=True)
