from django_tenants.utils import get_public_schema_name
from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from ..models import Facility, FacilityDomain
from .filters import FacilityFilter
from .serializers import FacilitySerializer
from apps.facility_tenant.rest_api.views import (
    SessionView as BaseSessionView,
    GlobalConfView as BaseGlobalConfView
)


class SessionView(BaseSessionView):
    pass


class GlobalConfView(BaseGlobalConfView):
    pass


class FacilityView(viewsets.ReadOnlyModelViewSet):
    max_page_size = 0
    queryset = Facility.objects.all()
    serializer_class = FacilitySerializer
    filterset_class = FacilityFilter
    permission_classes = (permissions.AllowAny,)
    ordering = 'id'
    ordering_fields = '__all__'
    search_fields = ['name', 'description', 'address', 'phone_number', 'email']

    def get_queryset(self):
        public_schema = get_public_schema_name()
        return super().get_queryset().exclude(schema_name=public_schema).prefetch_related('domains')

    @action(detail=False, url_path='domain/(?P<domain>[\w-]+)')
    def domain(self, request, *args, **kwargs):
        obj = get_object_or_404(FacilityDomain.objects, domain=kwargs.get('domain'))
        return Response(self.serializer_class(obj.tenant, context={'request': request}).data)
