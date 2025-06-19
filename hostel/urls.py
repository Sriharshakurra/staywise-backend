# hostel/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('services/', views.services_view, name='services'),
]
