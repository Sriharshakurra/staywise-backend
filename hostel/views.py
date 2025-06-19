from django.shortcuts import render
from .models import Service

def services_view(request):
    services = Service.objects.all()
    return render(request, 'hostel/services.html', {'services': services})
