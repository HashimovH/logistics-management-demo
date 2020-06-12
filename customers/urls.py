from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.customers, name='customers'),
    path('/add', views.addCustomer, name="addCustomer"),
    path('/edit/<int:pk>', views.editCustomer, name="editCustomer"),
    path('/delete/<int:pk>', views.deleteCustomer, name="deleteCustomer"),
    path('/detail/<int:pk>', views.detailCustomer, name="detailCustomer"),
]
