import datetime
import functools
import logging
import os
import re
import sys
import traceback
import types
import uuid

import simplejson as json
from django.conf import settings
from django.db import connection
from django.urls import clear_url_caches, set_urlconf
from django_tenants.middleware import TenantSubfolderMiddleware as BaseTenantSubfolderMiddleware
from django_tenants.utils import get_public_schema_name, has_multi_type_tenants, get_tenant_model, \
    get_tenant_domain_model, get_subfolder_prefix

print = functools.partial(print, flush=True)


class DisableCSRFMiddleware(object):

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if getattr(settings, 'CSRF_DISABLED', False):
            setattr(request, '_dont_enforce_csrf_checks', True)

        response = self.get_response(request)
        return response


class InjectUiVersionInHeadersMiddleware(object):

    def __init__(self, get_response):
        self.get_response = get_response

    def _get_ui_version(self):
        ui_packages_path = os.path.join(settings.BASE_DIR, 'FRONTEND', 'human_aftercare_ui', 'package.json')
        if not os.path.exists(ui_packages_path):
            return
        version = None
        try:
            with open(ui_packages_path) as f:
                data = json.load(f)
            version = data.get('version')
        except Exception:
            traceback.print_exc()
        return version

    def __call__(self, request):
        response = self.get_response(request)
        ui_version = self._get_ui_version()
        if ui_version:
            response['X-UI-Version'] = ui_version
        else:
            print('Cannot discover UI version!')
        return response


class SqlQueryLogging:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        from sys import stdout
        if stdout.isatty():
            for query in connection.queries:
                print("\033[1;31m[%s]\033[0m \033[1m%s\033[0m" % (query['time'], " ".join(query['sql'].split())))
        return response


class RequestTimeLoggingMiddleware(object):
    """Middleware class logging request time to stderr.

    This class can be used to measure time of request processing
    within Django.  It can be also used to log time spent in
    middleware and in view itself, by putting middleware multiple
    times in INSTALLED_MIDDLEWARE.

    Static method `log_message' may be used independently of the
    middleware itself, outside of it, and even when middleware is not
    listed in INSTALLED_MIDDLEWARE.
    """

    @staticmethod
    def log_message(request, tag, message=''):
        """Log timing message to stderr.

        Logs message about `request' with a `tag' (a string, 10
        characters or less if possible), timing info and optional
        `message'.

        Log format is "timestamp tag uuid count path +delta message"
        - timestamp is microsecond timestamp of message
        - tag is the `tag' parameter
        - uuid is the UUID identifying request
        - count is number of logged message for this request
        - path is request.path
        - delta is timedelta between first logged message
          for this request and current message
        - message is the `message' parameter.
        """

        dt = datetime.datetime.utcnow()
        if not hasattr(request, '_logging_uuid'):
            request._logging_uuid = uuid.uuid1()
            request._logging_start_dt = dt
            request._logging_pass = 0

        request._logging_pass += 1
        print(
            u'%s %-10s %s %2d %s +%s %s' % (
                dt.isoformat(),
                tag,
                request._logging_uuid,
                request._logging_pass,
                request.path,
                dt - request._logging_start_dt,
                message,
            ), file=sys.stderr)

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if settings.DEBUG:
            self.log_message(request, 'request ')
        response = self.get_response(request)
        if settings.DEBUG:
            s = getattr(response, 'status_code', 0)
            r = str(s)
            if s in (300, 301, 302, 307):
                r += ' => %s' % response.get('Location', '?')
            elif getattr(response, 'content', None):
                r += ' (%db)' % len(response.content)
            self.log_message(request, 'response', r)
        return response


class TenantSubfolderMiddleware(BaseTenantSubfolderMiddleware):

    @staticmethod
    def _load_urlconf(tenant):
        import types
        from django.urls import re_path, include
        from importlib import import_module
        url_conf = import_module("{}".format(settings.ROOT_URLCONF))
        urlconf_module = types.ModuleType('{}{}'.format(settings.ROOT_URLCONF, tenant.id))
        subfolder_prefix = get_subfolder_prefix()
        urlconf_module.urlpatterns = [
            re_path(f'{subfolder_prefix}/{tenant.domain_subfolder}/', include(url_conf)),
        ]
        return urlconf_module

    def process_request(self, request):
        # Short circuit if tenant is already set by another middleware.
        # This allows for multiple tenant-resolving middleware chained together.
        if hasattr(request, "tenant"):
            return

        connection.set_schema_to_public()

        urlconf = None

        tenant_model = get_tenant_model()
        domain_model = get_tenant_domain_model()
        hostname = self.hostname_from_request(request)
        subfolder_prefix_path = "/{}/".format(get_subfolder_prefix())

        # We are in the public tenant
        if not request.path.startswith(subfolder_prefix_path):
            try:
                tenant = tenant_model.objects.get(schema_name=get_public_schema_name())
            except tenant_model.DoesNotExist:
                raise self.TENANT_NOT_FOUND_EXCEPTION("Unable to find public tenant")

            self.setup_url_routing(request)

        # We are in a specific tenant
        else:
            path_chunks = request.path[len(subfolder_prefix_path):].split("/")
            tenant_subfolder = path_chunks[0]
            try:
                tenant = self.get_tenant(domain_model=domain_model, hostname=tenant_subfolder)
            except domain_model.DoesNotExist:
                return self.no_tenant_found(request, hostname)

            tenant.domain_subfolder = tenant_subfolder
            urlconf = self._load_urlconf(tenant)

        tenant.domain_url = hostname
        request.tenant = tenant

        connection.set_tenant(request.tenant)
        clear_url_caches()  # Required to remove previous tenant prefix from cache, if present

        if urlconf:
            request.urlconf = urlconf
            set_urlconf(urlconf)

        settings.SESSION_COOKIE_NAME = '{}sessionid'.format(request.tenant.domain_subfolder or '')

    @staticmethod
    def setup_url_routing(request, force_public=False):
        """
        Sets the correct url conf based on the tenant
        :param request:
        :param force_public
        """
        public_schema_name = get_public_schema_name()
        if has_multi_type_tenants():
            return BaseTenantSubfolderMiddleware.setup_url_routing(request, force_public=force_public)

        # Do we have a public-specific urlconf?
        if (hasattr(settings, 'PUBLIC_SCHEMA_URLCONF') and
                (force_public or (not hasattr(request, 'tenant')) or
                 request.tenant.schema_name == get_public_schema_name())):
            request.urlconf = settings.PUBLIC_SCHEMA_URLCONF
