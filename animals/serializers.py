from rest_framework import serializers
from .models import *

class AnimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = RescuedAnimal
        fields = '__all__'

class AdoptionRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdoptionRequest
        fields = '__all__'

