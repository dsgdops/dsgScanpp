from django.shortcuts import render
from django.http import HttpResponse, request
from django.views.generic import ListView, TemplateView


class homeView(TemplateView):
    template_name = "dsgScanapp/home.html"





