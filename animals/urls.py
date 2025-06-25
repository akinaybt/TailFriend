from django.urls import path

from .views import *

urlpatterns = [
    path('rescued-animal-create/', RescuedAnimalCreateView.as_view()),
    path('rescued-animal-list/', RescuedAnimalListView.as_view()),
    path('adopt-pet/', AdoptionRequestCreateView.as_view()),
    path('adopt-pet-list/', AdoptionRequestListView.as_view()),
    path('adopt-pet-detail/<int:pk>/', AdoptionRequestDetailView.as_view()),
]