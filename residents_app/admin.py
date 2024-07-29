from django.contrib import admin
from .models import Resident, Building, Contract

# Include the models in the Django admin panel
admin.site.register(Resident)
admin.site.register(Building)
admin.site.register(Contract)