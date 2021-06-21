from django.contrib.auth import get_user_model
from django.db import models
from django.dispatch import receiver
from django_tenants.models import TenantMixin, DomainMixin
from django_tenants.signals import post_schema_sync
from django_tenants.utils import tenant_context
from phonenumber_field.modelfields import PhoneNumberField

User = get_user_model()


class Facility(TenantMixin):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=200)
    address = models.CharField(max_length=256, blank=True, null=True)
    phone_number = PhoneNumberField(null=True, blank=True, unique=True)
    email = models.EmailField(null=True, blank=True, unique=True)
    primary_contact_name = models.CharField(max_length=100, null=True, blank=True)
    primary_contact_phone = PhoneNumberField(null=True, blank=True)
    primary_contact_email = models.EmailField(null=True, blank=True)
    create_datetime = models.DateTimeField(auto_now_add=True)
    update_datetime = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'Facilities'

    def __str__(self):
        return self.schema_name


class FacilityDomain(DomainMixin):

    def __str__(self):
        return self.domain


@receiver(post_schema_sync, sender=TenantMixin)
def created_and_migrated_facility(sender, **kwargs):
    facility = kwargs['tenant']
    print(f"******** Initializing records for facility: [{facility}]", end='')
    with tenant_context(facility):
        User.objects.create_superuser(username='admin', password='test1234')
    print("[OK]")
