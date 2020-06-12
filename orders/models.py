from django.db import models
from customers.models import Customer
from vehicles.models import Vehicle
from services.models import Service
from django.contrib.auth.models import User
from accounts.models import Profile, Notification

# Create your models here.
class Order(models.Model):
    STATUS = (
        ('pending', 'Pending'),
        ('executing', 'Executing'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled')
    )

    PAYMENT = (
        ('Cash', 'Cash'),
        ('Credit Card', 'Credit Card')
    )

    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=255, choices=STATUS)
    price_purchase = models.DecimalField(max_digits=10, decimal_places=2)
    price_selling = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    executer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    service = models.ManyToManyField(Service)
    notes = models.TextField(null=True, blank=True)
    start = models.CharField(max_length=255, null=True, blank=True)
    destination = models.CharField(max_length=255, null=True, blank=True)
    payment_type = models.CharField(max_length=255, choices=PAYMENT, null=True, blank=True)
    qaime_no = models.CharField(max_length=255, null=True, blank=True)

    def save(self, *args, **kwargs):
        vehicle = Vehicle.objects.get(id=self.vehicle.id)
        print(vehicle.model)
        print(vehicle.status)
        if self.status == 'completed' or self.status == 'cancelled':
            vehicle.status = 'Free'
        else:
            vehicle.status = 'On The Way'
        print(vehicle.status)
        vehicle.save()

        user = User.objects.all()
        sharer = ''
        sharer = self.executer.first_name + ' ' + self.executer.last_name
        print(sharer)
        profile = Profile.objects.get(user=self.executer)
        for u in user:
            if self.pk is None:
                noteText = "Order for customer {} with {} has been added".format(self.customer.name, self.vehicle.model)
            else:
                noteText = "Order for customer {} with {} has been updated".format(self.customer.name, self.vehicle.model)
            redirectUrl = '/orders'
            n = Notification(user=u, who=sharer, profile_picture = profile.profile_picture, note=noteText, url=redirectUrl, where="order", read=False)
            n.save()
        super().save(*args, **kwargs)

