from django.urls import include, path
from rest_framework import routers

from .views import SessionView, ProfileView, GlobalConfView, ResidentView, FacilityView, UserView, GroupView, \
    PermissionView

rest_router = routers.DefaultRouter()
rest_router.trailing_slash = "/?"  # added to support both / and slashless
rest_router.register(r'session', SessionView, basename='session')
rest_router.register(r'me', ProfileView, basename='profile')
rest_router.register(r'accounts/user', UserView)
rest_router.register(r'accounts/group', GroupView)
rest_router.register(r'accounts/permission', PermissionView)
rest_router.register(r'facility', FacilityView, basename='facility')
rest_router.register(r'resident', ResidentView)
rest_router.register(r'global_conf', GlobalConfView, basename='global_conf')

app_name = 'facility_tenant'

urlpatterns = [
    path('', include(rest_router.urls))
]
