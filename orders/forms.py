from django.forms import ModelForm
from .models import Order
from django import forms

class OrderForm(ModelForm):
	class Meta:
		model = Order
		fields = ['customer', 'vehicle', 'service', 'price_purchase', 'status', 'price_selling','qaime_no' ,'notes', 'start', 'destination', 'payment_type']
