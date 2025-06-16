from django.db import models
from user.models import CustomUser


class RescuedAnimal(models.Model):
    SPECIES_CHOICES = [
        ('dog', 'Собака'),
        ('cat', 'Кошка'),
        ('other', 'Другое'),
    ]

    name = models.CharField(max_length=100)
    species = models.CharField(max_length=20, choices=SPECIES_CHOICES)
    custom_species = models.CharField(max_length=100, blank=True, null=True)  # пользователь вводит свой вариант
    breed = models.CharField(max_length=100, blank=True)
    age = models.PositiveIntegerField()
    health_status = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='rescued_animals/', blank=True)
    adopted = models.BooleanField(default=False)
    shelter = models.ForeignKey('shelter.Shelter', on_delete=models.CASCADE, related_name='animals')
    date_rescued = models.DateField()
    uploaded_by = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True)

    def get_species_display_name(self):
        if self.species == 'other' and self.custom_species:
            return self.custom_species
        return dict(self.SPECIES_CHOICES).get(self.species, 'Не указано')

    def __str__(self):
        return self.name

class AdoptionRequest(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='adoption_requests')
    rescued_animal = models.ForeignKey(RescuedAnimal, on_delete=models.CASCADE, related_name='adoption_requests')
    message = models.TextField(blank=True)
    date_requested = models.DateTimeField(auto_now_add=True)
