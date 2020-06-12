from django.shortcuts import render, redirect
from .models import Order
from .forms import OrderForm
from django.contrib import messages #Messages
from vehicles.models import Vehicle
from django.contrib.auth.decorators import login_required
from .filters import OrderFilter

# Create your views here.
@login_required(login_url='/login')
def orders(request):
    orders = Order.objects.all()
    myFilter = OrderFilter(request.GET, queryset=orders)
    orders = myFilter.qs
    context = {
        'orders': orders,
        'filter': myFilter
    }
    return render(request, 'orders/index.html', context)


@login_required(login_url='/login')
def addOrder(request):
    if request.method == 'POST':
        try:
            order = OrderForm(request.POST)
            new_order = order.save(commit=False)
            new_order.executer = request.user
            new_order.save()
            messages.success(request, 'Order has been created.')
        except:
            messages.error(request, 'Data is not valid')
        return redirect('orders')
    else:
        forms = OrderForm()
        context = {
            'form': forms
        }
        return render(request, 'orders/add.html', context)

@login_required(login_url='/login')
def editOrder(request, pk):
    order = Order.objects.get(id=pk)
    forms = OrderForm(instance=order)
    if request.method == 'POST':
        try:
            order = OrderForm(request.POST, instance=order)
            order.save()
            messages.success(request, 'Order has been updated.')
        except:
            messages.error(request, 'Data is not valid')
        return redirect('orders')
    
    context = {
        'form': forms
    }
    return render(request, 'orders/edit.html', context)

@login_required(login_url='/login')
def deleteOrder(request, pk):
    order = Order.objects.get(id=pk)
    can_delete = request.user.has_perm('orders.delete_customer')
    if can_delete == False:
        return redirect('deleteError')
    if request.method == 'POST':
        if order.delete():
            messages.success(request, 'Order has been deleted')
        else:
            messages.error(request, 'Order cannot been deleted')
        return redirect('orders')

            
    context = {
        'order': order
    }
    return render(request, 'orders/delete.html', context)

@login_required(login_url='/login')
def detailOrder(request, pk):
    order = Order.objects.get(id=pk)
    context = {
        'order': order
    }
    return render(request, 'orders/detail.html', context)
