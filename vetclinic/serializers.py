from .models import VeterinaryClinic, VetServices
from rest_framework import serializers

class VetClinicSerializer(serializers.ModelSerializer):
    class Meta:
        model = VeterinaryClinic
        fields = ['name', 'address', 'phone_number', 'email', 'website']

class VetServicesSerializer(serializers.ModelSerializer):
    clinic = serializers.StringRelatedField()
    class Meta:
        model = VetServices
        fields = ['clinic', 'service_name', 'price', 'description', 'is_available']
