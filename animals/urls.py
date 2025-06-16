from django.urls import path

from .views import *

urlpatterns = [
    path('rescued-animal-create/', RescuedAnimalCreateView.as_view()),
    path('rescued-animal-list/', RescuedAnimalListView.as_view()),
    path('adopt-pet/', AdoptionRequestView.as_view()),
]