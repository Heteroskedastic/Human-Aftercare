import jsonfield
from django.contrib.auth.password_validation import validate_password
from django.db import transaction
from rest_framework import serializers
from django.contrib.auth.models import Group, Permission
from django.core import exceptions as django_exceptions

from apps.facilities.models import User
from ..models import Resident, UserProfile
from human_aftercare.helpers.utils import DynamicFieldsSerializerMixin, Base64ImageField
from ...facilities.rest_api.serializers import FacilitySerializer

serializers.ModelSerializer.serializer_field_mapping[jsonfield.JSONField] = serializers.JSONField


class SessionSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=30)
    password = serializers.CharField(max_length=128, style={'input_type': 'password'})
    remember = serializers.BooleanField(initial=False, required=False)


class PermissionSerializer(DynamicFieldsSerializerMixin, serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = ('id', 'name', 'codename')


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


class ResidentSerializer(DynamicFieldsSerializerMixin, serializers.ModelSerializer):

    class Meta:
        model = Resident
        fields = '__all__'
