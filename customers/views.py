from django.shortcuts import render, redirect, get_object_or_404
from .models import Customer
from .forms import CustomerForm
from django.contrib import messages #Messages
from .filters import CustomerFilter
from orders.models import Order
from django.contrib.auth.decorators import login_required
from accounts.models import Notification

# Create your views here.
@login_required(login_url='/login')
def customers(request):
    customers = Customer.objects.all().order_by('-id')
    notifications = Notification.objects.all().filter(where='customer')
    for n in notifications:
        n.read = True
        n.save()
    myFilter = CustomerFilter(request.GET, queryset=customers)
    customers = myFilter.qs
    
    context = {
        'customers': customers,
        'filter': myFilter, 
    }
    return render(request, 'customers/customers.html', context)


@login_required(login_url='/login')
def addCustomer(request):
    if request.method == 'POST':
        try:
            customer = CustomerForm(request.POST)
            new_customer = customer.save(commit=False)
            new_customer.updated_by = request.user
            new_customer.save()
            messages.success(request, 'Customer has been created.')
        except:
            messages.error(request, 'Data is not valid')
        return redirect('customers')
    else:
        forms = CustomerForm()
        context = {
            'form': forms
        }
        return render(request, 'customers/add.html', context)

@login_required(login_url='/login')
def editCustomer(request, pk):
    customer = Customer.objects.get(id=pk)
    forms = CustomerForm(instance=customer)
    if request.method == 'POST':
        try:
            customer = CustomerForm(request.POST, instance=customer)
            customer.save()
            messages.success(request, 'Customer has been created.')
        except:
            messages.error(request, 'Data is not valid')
        return redirect('customers')
    
    context = {
        'form': forms
    }
    return render(request, 'customers/edit.html', context)

@login_required(login_url='/login')
def deleteCustomer(request, pk):
    customer = Customer.objects.get(id=pk)
    can_delete = request.user.has_perm('customers.delete_customer')
    if can_delete == False:
        return redirect('deleteError')
    if request.method == 'POST':
        if customer.delete():
            messages.success(request, 'Customer has been deleted')
        else:
            messages.error(request, 'Customer cannot been deleted')
        return redirect('customers')

            
    context = {
        'customer': customer
    }
    return render(request, 'customers/delete.html', context)

@login_required(login_url='/login')
def detailCustomer(request, pk):
    customer = get_object_or_404(Customer, id=pk)
    orders = Order.objects.all().filter(customer=customer)[:10]
    orderCount = Order.objects.all().filter(customer=customer).count()
    context = {
        'customer': customer,
        'orders': orders,
        'orderCount': orderCount
    }
    return render(request, 'customers/detail.html', context)