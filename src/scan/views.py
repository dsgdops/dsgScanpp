from django.shortcuts import render
from django.http import HttpResponse, request
from .models import scan
from django.views.generic import ListView, TemplateView
from . import script



class IndexView(ListView):
    template_name = 'scan/index.html'
    context_object_name = 'scan_list'

    def get_queryset(self):
        """Return the last five scans."""
        return scan.objects.order_by('-date')[:5]

def add_report(request):
    #q = scan(host="127.0.0.1", ports=script.run_scan("127.0.0.1"), date="2022-02-23")
    #q.save()
    return HttpResponse("Oui")



