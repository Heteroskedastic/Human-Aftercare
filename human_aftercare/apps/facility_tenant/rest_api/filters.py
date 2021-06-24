import operator
from functools import reduce

import django_filters
from django.contrib.auth.models import Permission, Group
from django.db.models import Q
from django_filters import rest_framework as filters
from django_filters.rest_framework import BooleanFilter

from ..models import Resident, User


class UserFilter(filters.FilterSet):
    min_date_joined = django_filters.IsoDateTimeFilter(field_name="date_joined", lookup_expr="gte")
    max_date_joined = django_filters.IsoDateTimeFilter(field_name="date_joined", lookup_expr="lte")
    min_last_login = django_filters.IsoDateTimeFilter(field_name="last_login", lookup_expr="gte")
    max_last_login = django_filters.IsoDateTimeFilter(field_name="last_login", lookup_expr="lte")
    name = django_filters.CharFilter(label='Name', method='name_method')

    def name_method(self, queryset, name, value):
        search_fields = ['first_name', 'last_name']
        query = reduce(operator.or_, (Q(**{'{}__icontains'.format(f): value}) for f in search_fields))
        return queryset.filter(query)

    class Meta:
        model = User
        fields = ['is_superuser', 'username', 'email', 'is_staff', 'is_active']


class GroupFilter(filters.FilterSet):
    ui_role = BooleanFilter(label='Ui Role?', method='ui_role_method')

    def ui_role_method(self, queryset, name, value):
        if value:
            queryset = queryset.filter(name__istartswith='uirole:')
        elif value is False:
            queryset = queryset.exclude(name__istartswith='uirole:')
        return queryset


    class Meta:
        model = Group
        fields = ['name']


class PermissionFilter(filters.FilterSet):
    codename = django_filters.BaseInFilter(field_name='codename')

    class Meta:
        model = Permission
        fields = ['name', 'codename']


class ResidentFilter(filters.FilterSet):

    class Meta:
        model = Resident
        fields = '__all__'
