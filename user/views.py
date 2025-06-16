from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from .serializers import  UserSerializer, UserProfileSerializer
from .permissions import IsProfileOrReadOnly
from .models import *

class UserRegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

class ProfileUpdateView(generics.RetrieveUpdateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated, IsProfileOrReadOnly]
    lookup_field = 'pk'
