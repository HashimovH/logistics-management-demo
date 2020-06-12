from django.shortcuts import render, redirect
from .models import Service
from .forms import ServiceForm
from django.contrib import messages #Messages
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/login')
def services(request):
    services = Service.objects.all()
    context = {
        'services': services,
    }
    return render(request, 'services/index.html', context)


@login_required(login_url='/login')
def addService(request):
    if request.method == 'POST':
        try:
            service = ServiceForm(request.POST)
            service.save()
            messages.success(request, 'Service has been created.')
        except:
            messages.error(request, 'Data is not valid')
        return redirect('services')
    else:
        forms = ServiceForm()
        context = {
            'form': forms
        }
        return render(request, 'services/add.html', context)

@login_required(login_url='/login')
def editService(request, pk):
    service = Service.objects.get(id=pk)
    forms = ServiceForm(instance=service)
    if request.method == 'POST':
        try:
            vehicle = ServiceForm(request.POST, instance=service)
            vehicle.save()
            messages.success(request, 'Service has been updated.')
        except:
            messages.error(request, 'Data is not valid')
        return redirect('services')
    
    context = {
        'form': forms
    }
    return render(request, 'services/edit.html', context)


@login_required(login_url='/login')
def deleteService(request, pk):
    service = Service.objects.get(id=pk)
    can_delete = request.user.has_perm('services.delete_customer')
    if can_delete == False:
        return redirect('deleteError')
    if request.method == 'POST':
        if service.delete():
            messages.success(request, 'Service has been deleted')
        else:
            messages.error(request, 'Service cannot been deleted')
        return redirect('services')

            
    context = {
        'service': service
    }
    return render(request, 'services/delete.html', context)