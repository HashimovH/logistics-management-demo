import django_filters
from django_filters import DateFilter, CharFilter
from .models import Customer

class CustomerFilter(django_filters.FilterSet):
    class Meta:
        model = Customer
        fields = ['updated_by']