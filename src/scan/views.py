from django.shortcuts import render
from django.http import HttpResponse
from .models import scan
from django.template import loader
from django.urls import reverse
from django.views import generic


class IndexView(generic.ListView):
    template_name = 'scan/index.html'
    context_object_name = 'scan_list'

    def get_queryset(self):
        """Return the last five scans."""
        return scan.objects.order_by('-date')[:5]