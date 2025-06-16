from django.contrib import admin
from .models import *

@admin.register(CustomUser)
class CustomUser(admin.ModelAdmin):
    list_display = ['first_name', 'last_name']

@admin.register(UserProfile)
class UserProfile(admin.ModelAdmin):
    list_display = ['user']

@admin.register(VetClinicUser)
class VetClinicUser(admin.ModelAdmin):
    list_display = ['user']

