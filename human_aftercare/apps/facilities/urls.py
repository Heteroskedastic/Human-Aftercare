from django.urls import re_path, path

from .views import (IndexView,)

app_name = 'facilities'

urlpatterns = [
    re_path(r'^$', IndexView.as_view(), name='index'),
]
