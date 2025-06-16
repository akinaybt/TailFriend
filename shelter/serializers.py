from rest_framework import serializers
from .models import Shelter

class ShelterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shelter
        fields = ['name', 'address', 'phone_number', 'email', 'website']
