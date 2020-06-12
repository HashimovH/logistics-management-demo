from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.vehicles, name='vehicles'),
    path('add/', views.addVehicle, name="addVehicle"),
    path('edit/<int:pk>', views.editVehicle, name="editVehicle"),
    path('delete/<int:pk>', views.deleteVehicle, name="deleteVehicle"),
    path('detail/<int:pk>', views.detailVehicle, name="detailVehicle"),

]
