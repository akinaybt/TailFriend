from django.db import models
import phonenumbers
import datetime
import pytz
from phonenumber_field.modelfields import PhoneNumberField

class VeterinaryClinic(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone_number = PhoneNumberField(unique=True)
    website = models.URLField(blank=True)
    email = models.EmailField(blank=True)
    latitude = models.DecimalField(max_digits=15, decimal_places=9)
    longitude = models.DecimalField(max_digits=15, decimal_places=9)
    is_open = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        # Get the current time in the clinic's timezone (replace 'Europe/Moscow' with the actual timezone)
        now = datetime.datetime.now(pytz.timezone('Europe/Moscow'))
        opening_hour = 9  # Replace with your actual opening hour
        closing_hour = 18  # Replace with your actual closing hour

        # Set is_open based on current time and opening hours. Handles overnight cases as well.
        if opening_hour <= now.hour < closing_hour:
            self.is_open = True
        else:
            self.is_open = False

        super().save(*args, **kwargs)  # Call the original save method

class VetServices(models.Model):
    clinic = models.ForeignKey(VeterinaryClinic, on_delete=models.CASCADE, related_name = 'services')
    service_name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    description = models.TextField()
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.service_name