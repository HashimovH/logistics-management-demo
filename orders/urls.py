from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.orders, name='orders'),
    path('/add/', views.addOrder, name="addOrder"),
    path('/edit/<int:pk>', views.editOrder, name="editOrder"),
    path('/delete/<int:pk>', views.deleteOrder, name="deleteOrder"),
    path('/detail/<int:pk>', views.detailOrder, name="detailOrder"),

]
