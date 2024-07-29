from django.urls import path
from . import views

# URL configuration
urlpatterns = [
    path('residents/', views.resident_list),
    path('contracts/', views.contract_list),
    path('buildings/', views.building_list),
]