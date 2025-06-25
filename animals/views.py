from rest_framework import generics
from .models import *
from .serializers import AnimalSerializer, AdoptionRequestSerializer
from user.permissions import IsVetworker

class RescuedAnimalCreateView(generics.CreateAPIView):
    queryset = RescuedAnimal.objects.all()
    serializer_class = AnimalSerializer

class RescuedAnimalListView(generics.ListAPIView):
    queryset = RescuedAnimal.objects.all()
    serializer_class = AnimalSerializer

class AdoptionRequestCreateView(generics.CreateAPIView):
    queryset = AdoptionRequest.objects.all()
    serializer_class = AdoptionRequestSerializer

class AdoptionRequestDetailView(generics.RetrieveAPIView):
    queryset = AdoptionRequest.objects.all()
    serializer_class = AdoptionRequestSerializer
    permission_classes = [IsVetworker]


class AdoptionRequestListView(generics.ListAPIView):
    queryset = AdoptionRequest.objects.all()
    serializer_class = AdoptionRequestSerializer
    permission_classes = [IsVetworker]