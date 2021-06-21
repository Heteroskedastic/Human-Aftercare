from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View


class IndexView(View):
    def get(self, request, *args, **kwargs):
        url_hash = "/fc/{}/".format(request.tenant.domain_subfolder)
        return redirect(reverse('ui-panel', kwargs={'hash': url_hash}))
