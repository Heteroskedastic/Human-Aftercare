import jsonfield
from django.conf import settings
from django.contrib.auth.hashers import make_password
from django.contrib.auth.password_validation import validate_password
from django.db import transaction
from rest_framework import serializers
from django.contrib.auth.models import Group, Permission
from django.core import exceptions as django_exceptions
from rest_framework.exceptions import PermissionDenied

from apps.facilities.models import User, Facility
from ..models import Resident, UserProfile, TherapyNote
from human_aftercare.helpers.utils import DynamicFieldsSerializerMixin, Base64ImageField, ex_reverse
from ...facilities.rest_api.serializers import FacilitySerializer

serializers.ModelSerializer.serializer_field_mapping[jsonfield.JSONField] = serializers.JSONField


class SessionSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=30)
    password = serializers.CharField(max_length=128, style={'input_type': 'password'})
    remember = serializers.BooleanField(initial=False, required=False)


class PermissionSerializer(DynamicFieldsSerializerMixin, serializers.ModelSerializer):
    app_label = serializers.CharField(read_only=True, source="content_type.app_label")

    class Meta:
        model = Permission
        fields = ('id', 'name', 'codename', "app_label")



class SetPasswordSerializer(serializers.Serializer):
    new_password = serializers.CharField(style={'input_type': 'password'})
    current_password = serializers.CharField(style={'input_type': 'password'})

    default_error_messages = {
        'invalid_password': 'Invalid Password',
    }

    def validate_current_password(self, value):
        is_password_valid = self.context['request'].user.check_password(value)
        if is_password_valid:
            return value
        else:
            self.fail('invalid_password')

    def validate_new_password(self, new_password):
        try:
            validate_password(new_password, self.context['request'].user)
        except django_exceptions.ValidationError as e:
            raise serializers.ValidationError({'new_password': list(e.messages)})
        return new_password


class NestedGroupSerializer(serializers.ModelSerializer):
    permissions = PermissionSerializer(read_only=True, many=True)

    class Meta:
        model = Group
        fields = ('id', 'name', 'permissions')


class NestedUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name')


class NestedUser2Serializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username',)


class NestedProfileSerializer(serializers.ModelSerializer):
    avatar = Base64ImageField(required=False, allow_null=True)
    class Meta:
        model = UserProfile
        fields = ('birth_date', 'gender', 'avatar')


class UserSessionSerializer(DynamicFieldsSerializerMixin, serializers.ModelSerializer):
    user_permissions = PermissionSerializer(read_only=True, many=True)
    groups = NestedGroupSerializer(read_only=True, many=True)
    facility = serializers.SerializerMethodField()
    profile = NestedProfileSerializer()

    def get_facility(self, obj):
        request = self.context.get('request')
        if request:
            return FacilitySerializer(request.tenant, context={'request': request}).data

    class Meta:
        model = User
        exclude = ('password',)


class UserProfileSerializer(DynamicFieldsSerializerMixin, serializers.ModelSerializer):
    profile = NestedProfileSerializer()

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email', 'last_login', 'is_superuser', 'username', 'is_staff',
                  'is_active', 'date_joined', 'profile',)
        read_only_fields = ('id', 'last_login', 'is_superuser', 'username', 'is_staff', 'is_active', 'date_joined')

    @transaction.atomic()
    def update(self, instance, validated_data):
        profile_object = getattr(instance, 'profile', None)
        if not profile_object:
            instance.profile = profile_object = UserProfile()
        profile = validated_data.pop('profile', {}) or {}
        for k, v in profile.items():
            setattr(profile_object, k, v)
        profile_object.save()

        return super().update(instance, validated_data)


class FacilitySerializer(DynamicFieldsSerializerMixin, serializers.ModelSerializer):
    url = serializers.SerializerMethodField()
    domain = serializers.SerializerMethodField()
    logo = Base64ImageField(required=False, allow_null=True)

    def get_url(self, obj):
        request = self.context.get('request')
        domain = self.get_domain(obj)
        return ex_reverse(f'/{settings.TENANT_SUBFOLDER_PREFIX}/{domain}/', request=request, scheme='auto')

    def get_domain(self, obj):
        domain = getattr(obj, 'domain_subfolder', None)
        if not domain:
            domain = obj.domains.filter(is_primary=True).first()
        return domain and str(domain)

    class Meta:
        model = Facility
        read_only_fields = ['schema_name', 'is_active']
        fields = '__all__'


class UserSerializer(DynamicFieldsSerializerMixin, serializers.ModelSerializer):
    profile = NestedProfileSerializer(read_only=True)
    _groups = NestedGroupSerializer(read_only=True, source='groups', many=True)
    _user_permissions = PermissionSerializer(read_only=True, source='user_permissions', many=True)

    class Meta:
        model = User
        fields = ('id', 'last_login', 'username', 'first_name', 'last_name', 'email', 'is_staff', 'is_superuser',
                  'is_active', 'date_joined', 'groups', 'user_permissions', 'profile', '_groups', '_user_permissions')
        read_only_fields = ('last_login', 'date_joined')


class ChangePasswordSerializer(serializers.Serializer):
    password = serializers.CharField(style={'input_type': 'password'})


class GroupSerializer(DynamicFieldsSerializerMixin, serializers.ModelSerializer):
    _permissions = PermissionSerializer(read_only=True, source='permissions', many=True)
    permissions_count = serializers.SerializerMethodField(read_only=True)
    UIROLE_PREFIX = 'uirole:'

    class Meta:
        model = Group
        fields = ('id', 'name', 'permissions', '_permissions', 'permissions_count')

    def get_permissions_count(self, obj):
        return obj.permissions.count()

    def validate_name(self, value):
        if not self.instance and value.lower().startswith(self.UIROLE_PREFIX):
            raise PermissionDenied('cannot add a group name starting with "UIrole:"')

        return value


class ResidentSerializer(DynamicFieldsSerializerMixin, serializers.ModelSerializer):
    photo = Base64ImageField(required=False, allow_null=True)

    class Meta:
        model = Resident
        fields = '__all__'


class NestedResidentSerializer(DynamicFieldsSerializerMixin, serializers.ModelSerializer):

    class Meta:
        model = Resident
        fields = ('id', 'first_name', 'last_name')


class TherapyNoteSerializer(DynamicFieldsSerializerMixin, serializers.ModelSerializer):
    _create_by = NestedUser2Serializer(read_only=True, source='create_by')
    _update_by = NestedUser2Serializer(read_only=True, source='update_by')
    _resident = NestedResidentSerializer(read_only=True, source='resident')

    class Meta:
        model = TherapyNote
        fields = '__all__'
