from django.shortcuts import render, HttpResponse
from crimes.models import CrimeTable

def index(request):
    crimes = CrimeTable.objects.filter(lat__icontains = '.')
    return render(request,  'crimes/index.html', {'crimes':crimes})
