from django.shortcuts import render
from .models import Service

def services_view(request):
    services = Service.objects.all()
    return render(request, 'hostel/services.html', {'services': services})

def home_view(request):
    return render(request, 'hostel/home.html')
