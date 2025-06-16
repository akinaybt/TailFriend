from django.contrib import admin
from .models import VeterinaryClinic, VetServices

@admin.register(VeterinaryClinic)
class Clinic(admin.ModelAdmin):
    list_display = ['name', 'address']


@admin.register(VetServices)
class Service(admin.ModelAdmin):
    list_display = ['service_name']
