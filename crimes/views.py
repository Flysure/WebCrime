from django.shortcuts import render, HttpResponse
from crimes.models import CrimeTable
from .forms import crimeForm

def index(request):
    crimes = CrimeTable.objects.filter(lat__icontains = '.')
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = crimeForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            return render(request,  'crimes/index.html', {'crimes':crimes, 'form':form})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = crimeForm()

    return render(request,  'crimes/index.html', {'crimes':crimes, 'form':form})
