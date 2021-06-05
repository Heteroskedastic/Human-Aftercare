from django_filters import rest_framework as filters

from ..models import Resident


class ResidentFilter(filters.FilterSet):

    class Meta:
        model = Resident
        fields = '__all__'
