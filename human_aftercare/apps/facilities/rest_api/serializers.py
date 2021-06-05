from django.conf import settings
from rest_framework import serializers

from apps.facilities.models import Facility
from human_aftercare.helpers.utils import DynamicFieldsSerializerMixin, ex_reverse


class FacilitySerializer(DynamicFieldsSerializerMixin, serializers.ModelSerializer):
    url = serializers.SerializerMethodField()

    def get_url(self, obj):
        request = self.context.get('request')
        domain = obj.domains.filter(is_primary=True).first()
        if not domain:
            return None
        return ex_reverse(f'/{settings.TENANT_SUBFOLDER_PREFIX}/{domain.domain}/', request=request, scheme='auto')

    class Meta:
        model = Facility
        exclude = ['primary_contact_name', 'primary_contact_phone', 'primary_contact_email', 'update_datetime',]
