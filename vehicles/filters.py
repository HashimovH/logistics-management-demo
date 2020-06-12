import django_filters
from django_filters import DateFilter, CharFilter
from .models import Vehicle

class VehicleFilter(django_filters.FilterSet):
    class Meta:
        model = Vehicle
        fields = ['type_car', 'capacity', 'updated_by']