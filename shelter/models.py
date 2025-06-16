from django.db import models

class Shelter(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    website = models.URLField(blank=True)
    email = models.EmailField(blank=True)
    latitude = models.DecimalField(max_digits=15, decimal_places=9)
    longitude = models.DecimalField(max_digits=15, decimal_places=9)
    is_open = models.BooleanField(default=True)

    def __str__(self):
        return self.name

