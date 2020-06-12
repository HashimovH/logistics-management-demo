import django_filters
from django_filters import DateFilter, CharFilter
from .models import Order

class OrderFilter(django_filters.FilterSet):
    class Meta:
        model = Order
        fields = ['customer', 'vehicle', 'executer', 'service', 'status']