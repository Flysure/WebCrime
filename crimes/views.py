from django.shortcuts import render, HttpResponse
from crimes.models import CrimeTable
from .forms import crimeForm
import datetime

def index(request):

    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = crimeForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            beg = form.cleaned_data['date_reported_beg']
            end = form.cleaned_data['date_reported_end']
            beg = datetime.datetime.strptime(str(beg), '%Y-%m-%d').strftime('%m/%d/%y')
            end = datetime.datetime.strptime(str(end), '%Y-%m-%d').strftime('%m/%d/%y')
            crimes = CrimeTable.objects.filter( datereported__range = [beg, end], lat__icontains = '.' )
            return render(request,  'crimes/index.html', {'crimes':crimes, 'form':form})

    # if a GET (or any other method) we'll create a blank form
    else:
        crimes = CrimeTable.objects.filter(lat__icontains = '.')
        form = crimeForm()

    return render(request,  'crimes/index.html', {'crimes':crimes, 'form':form})
