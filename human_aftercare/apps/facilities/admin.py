from django.contrib import admin
from django_tenants.utils import get_public_schema_name

from .models import Facility, FacilityDomain


class DomainInline(admin.TabularInline):
    model = FacilityDomain


class FacilityAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'schema_name', 'description', 'email', 'phone_number', 'is_active')
    search_fields = ('name', 'schema_name', 'description', 'email', 'phone_number')
    inlines = [DomainInline]

    def get_queryset(self, request):
        public_schema = get_public_schema_name()
        return super().get_queryset(request).exclude(schema_name=public_schema)


admin.site.register(Facility, FacilityAdmin)
