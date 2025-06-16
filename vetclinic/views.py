from rest_framework import generics, status
from rest_framework.permissions import AllowAny, IsAdminUser
from .serializers import VetClinicSerializer, VetServicesSerializer
from .models import *

class VetClinicView(generics.ListAPIView):
    queryset = VeterinaryClinic.objects.all()
    permission_classes = [AllowAny]
    serializer_class = VetClinicSerializer

class VetServicesView(generics.ListAPIView):
    queryset = VetServices.objects.all()
    permission_classes = [AllowAny]
    serializer_class = VetServicesSerializer

