from django.urls import include, path
from rest_framework import routers

from .views import SessionView, GlobalConfView, FacilityView

rest_router = routers.DefaultRouter()
rest_router.trailing_slash = "/?"  # added to support both / and slashless
rest_router.register(r'session', SessionView, basename='session')
rest_router.register(r'facility', FacilityView)
rest_router.register(r'global_conf', GlobalConfView, basename='global_conf')

app_name = 'facilities'

urlpatterns = [
    path('', include(rest_router.urls))
]
