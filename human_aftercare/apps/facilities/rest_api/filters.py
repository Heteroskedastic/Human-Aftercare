from django_filters import rest_framework as filters

from ..models import Facility


class FacilityFilter(filters.FilterSet):

    class Meta:
        model = Facility
        exclude = ['primary_contact_name', 'primary_contact_phone', 'primary_contact_email', 'logo']

