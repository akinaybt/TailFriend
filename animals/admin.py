from django.contrib import admin
from .models import *

@admin.register(RescuedAnimal)
class RescuedAnimal(admin.ModelAdmin):
    list_display = ['name', 'species', 'breed']

@admin.register(AdoptionRequest)
class AdoptionRequest(admin.ModelAdmin):
    list_display = ['user', 'rescued_animal']