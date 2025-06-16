from django.urls import path

from .views import *

urlpatterns = [
    path('list-shelters', ShelterListView.as_view()),
    path('shelter-detail/<int:pk>/', ShelterDetailView.as_view()),
]