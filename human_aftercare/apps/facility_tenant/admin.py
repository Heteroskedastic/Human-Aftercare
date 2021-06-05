from django.contrib import admin
from django.contrib.auth.admin import UserAdmin, GroupAdmin
from django.contrib.auth.models import User, Group

from .models import Resident


class FacilityTenantAdminSite(admin.AdminSite):
    site_header = "Facility Admin"
    site_title = "Facility Admin Panel"
    index_title = "Facility Admin Panel"


class ResidentAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'middle_name', 'last_name', 'birth_date', 'gender')
    search_fields = ('first_name', 'middle_name', 'last_name')


site = FacilityTenantAdminSite(name='facility_tenant_admin')
site.register(User, UserAdmin)
site.register(Group, GroupAdmin)
site.register(Resident, ResidentAdmin)

