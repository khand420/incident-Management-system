

from django.contrib.auth.models import AbstractUser
from django.db import models
import random
from django.conf import settings
from datetime import datetime



class User(AbstractUser):
    phone_number = models.CharField(max_length=15, unique=True)
    address = models.TextField()
    pin_code = models.CharField(max_length=10)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)






def generate_incident_id():
    current_year = datetime.now().year
    return f"RMG{random.randint(10000, 99999)}{current_year}"

class Incident(models.Model):
    ENTERPRISE = 'Enterprise'   
    GOVERNMENT = 'Government'
    REPORTER_CHOICES = [
        (ENTERPRISE, 'Enterprise'),
        (GOVERNMENT, 'Government'),
    ]

    STATUS_CHOICES = [
        ('Open', 'Open'),
        ('In Progress', 'In Progress'),
        ('Closed', 'Closed'),
    ]

    PRIORITY_CHOICES = [
        ('High', 'High'),
        ('Medium', 'Medium'),
        ('Low', 'Low'),
    ]

    incident_id = models.CharField(max_length=15, unique=True, default=generate_incident_id)
    reporter = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    reporter_type = models.CharField(max_length=50, choices=REPORTER_CHOICES)
    details = models.TextField()
    reported_date = models.DateTimeField(auto_now_add=True)
    priority = models.CharField(max_length=50, choices=PRIORITY_CHOICES)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES)

    def save(self, *args, **kwargs):
        # Ensure unique incident_id
        if not self.incident_id:
            self.incident_id = generate_incident_id()
        super().save(*args, **kwargs)


