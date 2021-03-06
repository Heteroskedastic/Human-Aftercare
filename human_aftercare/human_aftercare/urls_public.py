"""human_aftercare URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path, re_path, include
from django.views.static import serve
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token

from apps.facilities.views import UiPanelView

VERSION_PARAM = settings.REST_FRAMEWORK.get('VERSION_PARAM', 'version')
DEFAULT_VERSION = settings.REST_FRAMEWORK.get('DEFAULT_VERSION', 'v1')
API_ENDPOINT = 'api/(?P<{}>v\d+)'.format(VERSION_PARAM)

urlpatterns = [
    path('', include('apps.facilities.urls', namespace='facilities')),
    re_path('^{}/'.format(API_ENDPOINT),
            include('apps.facilities.rest_api.urls', namespace='facilities_rest_api')),
    path('admin/', admin.site.urls),
    re_path(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    re_path(r'^token/auth/', obtain_jwt_token),
    re_path(r'^token/refresh/', refresh_jwt_token),
    re_path(r'^token/verify/', verify_jwt_token),
    re_path(r'^ui-panel(?:(?P<hash>\S+))?$', UiPanelView.as_view(), name='ui-panel'),
]

if settings.DEBUG:
    urlpatterns += [
        re_path(r'^media/(.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    ]
