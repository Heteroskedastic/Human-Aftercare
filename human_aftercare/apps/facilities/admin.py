from django.contrib import admin

from .models import Facility, FacilityDomain


class DomainInline(admin.TabularInline):
    model = FacilityDomain


class FacilityAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'schema_name', 'description', 'email', 'phone_number', 'is_active')
    search_fields = ('name', 'schema_name', 'description', 'email', 'phone_number')
    inlines = [DomainInline]


admin.site.register(Facility, FacilityAdmin)
