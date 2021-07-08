from django.conf import settings
from django.contrib.auth.models import Permission, Group
from rest_framework import serializers

from apps.facilities.models import Facility, User
from human_aftercare.helpers.utils import DynamicFieldsSerializerMixin, ex_reverse



class PermissionSerializer(DynamicFieldsSerializerMixin, serializers.ModelSerializer):
    app_label = serializers.CharField(read_only=True, source="content_type.app_label")

    class Meta:
        model = Permission
        fields = ('id', 'name', 'codename', "app_label")


class NestedGroupSerializer(serializers.ModelSerializer):
    permissions = PermissionSerializer(read_only=True, many=True)

    class Meta:
        model = Group
        fields = ('id', 'name', 'permissions')


class UserSessionSerializer(DynamicFieldsSerializerMixin, serializers.ModelSerializer):
    user_permissions = PermissionSerializer(read_only=True, many=True)
    groups = NestedGroupSerializer(read_only=True, many=True)

    class Meta:
        model = User
        exclude = ('password',)



class FacilitySerializer(DynamicFieldsSerializerMixin, serializers.ModelSerializer):
    url = serializers.SerializerMethodField()
    domain = serializers.SerializerMethodField()

    def get_url(self, obj):
        request = self.context.get('request')
        domain = obj.domains.filter(is_primary=True).first()
        if not domain:
            return None
        return ex_reverse(f'/{settings.TENANT_SUBFOLDER_PREFIX}/{domain.domain}/', request=request, scheme='auto')

    def get_domain(self, obj):
        domain = getattr(obj, 'domain_subfolder', None)
        if not domain:
            domain = obj.domains.filter(is_primary=True).first()
        return domain and str(domain)

    class Meta:
        model = Facility
        exclude = ['primary_contact_name', 'primary_contact_phone', 'primary_contact_email', 'update_datetime',]
