from django.db import models
from django.contrib.auth.models import User


class EmergencyService(models.Model):
    """
    Represents available emergency services with their details.
    """

    SERVICE_CHOICES = [
        ('Ambulance', 'Ambulance'),
        ('Paramedics', 'Paramedics'),
    ]

    service_type = models.CharField(max_length=20, choices=SERVICE_CHOICES)
    cost = models.IntegerField()
    ETA = models.CharField(max_length=20)  # Estimated Time of Arrival

    def __str__(self):
        return self.service_type


class EmergencyServiceRequest(models.Model):
    """
    Represents a patient's request to utilize an emergency service.
    """

    PENDING = 'Pending'
    APPROVED = 'Approved'
    REJECTED = 'Rejected'
    STATUS_CHOICES = [
        (PENDING, 'Pending'),
        (APPROVED, 'Approved'),
        (REJECTED, 'Rejected'),
    ]

    patient = models.ForeignKey(User, on_delete=models.CASCADE)
    service = models.ForeignKey(EmergencyService, on_delete=models.CASCADE)
    request_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=PENDING)

    def __str__(self):
        return f"{self.patient}'s request for {self.service}"
