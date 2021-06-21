from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View

class IndexView(View):

    def get(self, request, *args, **kwargs):
        ctx = {}
        return redirect(reverse('ui-panel'))


class UiPanelView(View):
    def get(self, request, *args, **kwargs):
        hash = kwargs.get('hash') or ''
        url = '/static/vue/index.html'
        if hash:
            url += '#{}'.format(hash)
        qs = request.GET.urlencode()
        if qs:
            url += '?' + qs
        return redirect(url)
