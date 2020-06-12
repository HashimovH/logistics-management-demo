from django.shortcuts import render, redirect, get_object_or_404
from .models import Vehicle
from .forms import VehicleForm
from django.contrib import messages #Messages
from .filters import VehicleFilter
from django.contrib.auth.decorators import login_required
from accounts.models import Notification
from orders.models import Order

# Create your views here.
@login_required(login_url='/login')
def vehicles(request):
    vehicles = Vehicle.objects.all()
    notifications = Notification.objects.all().filter(where='vehicle')
    for n in notifications:
        n.read = True
        n.save()
    myFilter = VehicleFilter(request.GET, queryset=vehicles)
    vehicles = myFilter.qs
    context = {
        'vehicles': vehicles,
        'filter': myFilter
    }
    return render(request, 'vehicles/index.html', context)

@login_required(login_url='/login')
def addVehicle(request):
    if request.method == 'POST':
        try:
            vehicle = VehicleForm(request.POST)
            new_vehicle = vehicle.save(commit=False)
            new_vehicle.updated_by = request.user
            new_vehicle.save()
            messages.success(request, 'Vehicle has been created.')
        except:
            messages.error(request, 'Data is not valid')
        return redirect('vehicles')
    else:
        forms = VehicleForm()
        context = {
            'form': forms
        }
        return render(request, 'vehicles/add.html', context)

@login_required(login_url='/login')
def editVehicle(request, pk):
    vehicle = Vehicle.objects.get(id=pk)
    forms = VehicleForm(instance=vehicle)
    if request.method == 'POST':
        try:
            vehicle = VehicleForm(request.POST, instance=vehicle)
            vehicle.save()
            messages.success(request, 'Vehicle has been updated.')
        except:
            messages.error(request, 'Data is not valid')
        return redirect('vehicles')
    
    context = {
        'form': forms
    }
    return render(request, 'vehicles/edit.html', context)

@login_required(login_url='/login')
def deleteVehicle(request, pk):
    vehicle = Vehicle.objects.get(id=pk)
    can_delete = request.user.has_perm('vehicle.delete_customer')
    if can_delete == False:
        return redirect('deleteError')
    if request.method == 'POST':
        if vehicle.delete():
            messages.success(request, 'Vehicle has been deleted')
        else:
            messages.error(request, 'Vehicle cannot been deleted')
        return redirect('vehicles')

            
    context = {
        'vehicle': vehicle
    }
    return render(request, 'vehicles/delete.html', context)

@login_required(login_url='/login')
def detailVehicle(request, pk):
    vehicle = get_object_or_404(Vehicle, id=pk)
    orders = Order.objects.all().filter(vehicle=vehicle).order_by('-id')[:5]
    context = {
        'vehicle': vehicle,
        'orders': orders
    }
    return render(request, 'vehicles/detail.html', context)