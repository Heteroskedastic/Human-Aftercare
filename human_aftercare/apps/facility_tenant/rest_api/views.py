from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group, Permission
from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.exceptions import PermissionDenied
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response

from human_aftercare.helpers.utils import ExplicitPermissions
from .filters import ResidentFilter, UserFilter, GroupFilter, PermissionFilter
from .serializers import SessionSerializer, UserSessionSerializer, UserProfileSerializer, \
    SetPasswordSerializer, ResidentSerializer, FacilitySerializer, UserSerializer, GroupSerializer, \
    PermissionSerializer, ChangePasswordSerializer
from ..models import Resident, User


class SessionView(viewsets.ViewSet):
    getterSerializer = UserSessionSerializer

    class SessionPermission(permissions.BasePermission):
        """ custom class to check permissions for sessions """

        def has_permission(self, request, view):
            """ check request permissions """
            if request.method == 'POST':
                return True
            return request.user.is_authenticated and request.user.is_active

    permission_classes = (SessionPermission,)
    serializer_class = SessionSerializer

    def get(self, request, *args, **kwargs):
        """ api to get current session """
        return Response(self.getterSerializer(request.user, context={'request': request}).data)

    def post(self, request, *args, **kwargs):
        """ api to login """
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = authenticate(**serializer.data)
        if not user:
            return Response({'detail': 'Username or password is incorrect'}, status=status.HTTP_400_BAD_REQUEST)
        if not user.is_active:
            return Response({'detail': 'User is inactive'}, status=status.HTTP_403_FORBIDDEN)

        login(request, user)
        return Response(self.getterSerializer(user, context={'request': request}).data)

    def delete(self, request, *args, **kwargs):
        """ api to logout """

        user_id = request.user.id
        logout(request)
        return Response({'id': user_id})

    create = post  # this is a trick to show this view in api-root


class ProfileView(viewsets.ViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = UserProfileSerializer
    parser_classes = list(viewsets.ViewSet.parser_classes) + [FileUploadParser]

    def list(self, request, *args, **kwargs):
        return Response(self.serializer_class(request.user, context={'request': request}).data)

    def put(self, request, *args, **kwargs):
        serializer = self.serializer_class(instance=request.user, data=request.data, partial=True,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    @action(detail=False, methods=['PUT'])
    def password(self, request, *args, **kwargs):
        serializer = SetPasswordSerializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        self.request.user.set_password(serializer.validated_data['new_password'])
        self.request.user.save(update_fields=['password'])

        return Response(status=status.HTTP_204_NO_CONTENT)

    create = put


class FacilityView(viewsets.ViewSet):
    permission_classes = (permissions.IsAuthenticated, ExplicitPermissions)
    serializer_class = FacilitySerializer
    parser_classes = list(viewsets.ViewSet.parser_classes) + [FileUploadParser]
    explicit_permissions = {
        'list': ['facilities.view_facility'],
        'put': ['facilities.change_facility'],
        'create': ['facilities.change_facility'],
    }

    def list(self, request, *args, **kwargs):
        return Response(self.serializer_class(request.tenant, context={'request': request}).data)

    def put(self, request, *args, **kwargs):
        serializer = self.serializer_class(instance=request.tenant, data=request.data, partial=True,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    create = put


class UserView(viewsets.ModelViewSet):
    max_page_size = 0
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filterset_class = UserFilter
    ordering = 'id'
    ordering_fields = ('id', 'last_login', 'is_superuser', 'username', 'first_name', 'last_name', 'email', 'is_staff',
                       'is_active', 'date_joined')
    search_fields = ['username', 'first_name', 'last_name', 'email']

    @action(detail=True, methods=['put'], serializer_class=ChangePasswordSerializer)
    def set_password(self, request, *args, **kwargs):
        user = self.get_object()
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user.set_password(serializer.data['password'])
        user.save()
        return Response(status=status.HTTP_204_NO_CONTENT)


class GroupView(viewsets.ModelViewSet):
    max_page_size = 0
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    filterset_class = GroupFilter
    ordering = 'id'
    ordering_fields = ('id', 'name')
    search_fields = ['name']

    def __check_ui_role_for_update(self):
        instance = self.get_object()
        if instance.name.lower().startswith(GroupSerializer.UIROLE_PREFIX):
            raise PermissionDenied('cannot modify or delete a "UIrole" group')

    def update(self, request, *args, **kwargs):
        self.__check_ui_role_for_update()
        return super(GroupView, self).update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        self.__check_ui_role_for_update()
        return super(GroupView, self).destroy(request, *args, **kwargs)


class PermissionView(viewsets.ReadOnlyModelViewSet):
    max_page_size = 0
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer
    filterset_class = PermissionFilter
    ordering = 'id'
    ordering_fields = ('id', 'name', 'codename')


class ResidentView(viewsets.ModelViewSet):
    queryset = Resident.objects.all()
    serializer_class = ResidentSerializer
    filterset_class = ResidentFilter
    ordering = 'id'
    ordering_fields = '__all__'
    search_fields = ['first_name', 'middle_name', 'last_name']


class GlobalConfView(viewsets.ViewSet):
    PUBLIC_KEYS = ['TIME_ZONE',]
    LOGIN_REQUIRED_KEYS = []
    permission_classes = (permissions.AllowAny,)

    @property
    def conf_keys(self):
        keys = self.PUBLIC_KEYS
        if self.request.user.is_authenticated:
            keys += self.LOGIN_REQUIRED_KEYS
        return keys

    def get(self, request, *args, **kwargs):
        configs = {c: getattr(settings, c, None) for c in self.conf_keys}
        return Response(configs)

    def retrieve(self, request, *args, **kwargs):
        conf_key = kwargs.get('pk')
        if conf_key not in self.conf_keys:
            return Response(status=status.HTTP_404_NOT_FOUND)

        return Response(getattr(settings, conf_key, None))

    def create(self, request, *args, **kwargs):
        # this method is a trick to show this view in api-root
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
