from django.shortcuts import render
from .models import Resident, Building, Contract

# Function to read and render the resident list
def resident_list(request):
    residents = Resident.objects.all()
    return render(request, 'resident_list.html', {'residents': residents})

# Function to read and render the list of contracts
def contract_list(request):
    contracts = Contract.objects.all()
    return render(request, 'contract_list.html', {'contracts': contracts})

# Function to render the list of buildings
def building_list(request):
    buildings = Building.objects.all()
    return render(request, 'building_list.html', {'buildings': buildings})
