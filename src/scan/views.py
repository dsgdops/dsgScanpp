from django.shortcuts import render
from django.http import HttpResponse
from .models import scan

def index(request):
    latest_scan_list = scan.objects.order_by('-date')[:5]
    output = ', '.join([q.host for q in latest_scan_list])
    return HttpResponse(output)