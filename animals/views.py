from rest_framework import generics
from .models import *
from .serializers import AnimalSerializer, AdoptionRequestSerializer


class RescuedAnimalCreateView(generics.CreateAPIView):
    queryset = RescuedAnimal.objects.all()
    serializer_class = AnimalSerializer

class RescuedAnimalListView(generics.ListAPIView):
    queryset = RescuedAnimal.objects.all()
    serializer_class = AnimalSerializer

class AdoptionRequestView(generics.CreateAPIView):
    queryset = AdoptionRequest.objects.all()
    serializer_class = AdoptionRequestSerializer
