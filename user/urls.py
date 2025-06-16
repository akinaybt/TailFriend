from django.urls import path
from .views import *
urlpatterns = [
    path('registration/', UserRegisterView.as_view()),
    path('profile-update/<int:pk>/', ProfileUpdateView.as_view()),

]
