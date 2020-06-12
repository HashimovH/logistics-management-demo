from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.services, name='services'),
    path('/add/', views.addService, name="addService"),
    path('/edit/<int:pk>', views.editService, name="editService"),
    path('/delete/<int:pk>', views.deleteService, name="deleteService")
]
