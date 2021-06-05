from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class FacilityTenantConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.facility_tenant'
    verbose_name = _("Facility")
