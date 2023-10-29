from django.db import models

class HospitalBeds(models.Model):
    """
    Model for hospital beds.
    """
    CATEGORY_CHOICES = [
        ('ICU', 'ICU'),
        ('CCU', 'CCU'),
        ('HDU', 'HDU'),
        ('VIP', 'VIP'),
        ('Deluxe Suite', 'Deluxe Suite'),
        ('Standard Suite', 'Standard Suite'),
        ('Deluxe Single', 'Deluxe Single'),
        ('Luxury Single', 'Luxury Single'),
        ('Standard Single', 'Standard Single'),
        ('Double Bedded Room (per bed)', 'Double Bedded Room (per bed)'),
        ('General Ward (Female)', 'General Ward (Female)'),
        ('General Ward (Male)', 'General Ward (Male)'),
        # Add more categories as needed
    ]

    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    position = models.CharField(max_length=10, unique=True)  # Assuming position is unique
    rent_per_day = models.FloatField()
    is_available = models.BooleanField(default=True)  # For availability status

    def __str__(self):
        """
        String representation of a HospitalBeds instance.

        Returns:
            str: String representation of position and category.
        """
        return f"{self.position} - {self.category}"









