from django.db import models
from datetime import date, timedelta

class Registration(models.Model):
    # Existing fields
    name = models.CharField(max_length=255)
    gender = models.CharField(max_length=10)
    dob = models.DateField()
    weight = models.CharField(max_length=10)
    blood_group = models.CharField(max_length=5)
    email = models.EmailField()
    phone = models.CharField(max_length=10, unique=True)
    last_donation_date = models.DateField(null=True, blank=True)
    ward_numbers = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Registrations"

    def is_active(self):
        if self.last_donation_date:
            # Calculate the date three months ago from today
            three_months_ago = date.today() - timedelta(days=3 * 30)
            return self.last_donation_date <= three_months_ago
        return False
