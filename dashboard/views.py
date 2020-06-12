from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from vehicles.models import Vehicle
from orders.models import Order
from customers.models import Customer

# Create your views here.
@login_required(login_url="/login")
def dashboard(request):
    total_customers = Customer.objects.all().count()
    total_vehicles = Vehicle.objects.all().count()
    total_orders = Order.objects.all().count()
    completed_orders = Order.objects.all().filter(status='Completed').count()

    orders = Order.objects.all()
    last_5 = orders.order_by('-id')[:5]
    executing = orders.filter(status='executing').order_by('-id')[:5]

    context = {
        'total_customers': total_customers,
        'total_vehicles': total_vehicles,
        'total_orders': total_orders,
        'completed_orders': completed_orders,
        'last_5': last_5,
        'executing': executing,
        'dashboard': 'open'
    }
    return render(request, 'dashboard/home.html', context)