from django.urls import path, include
from . import views

urlpatterns = [
     path('vetclinic-list/', views.VetClinicView.as_view()),
     path('service-list/', views.VetServicesView.as_view()),
 ]