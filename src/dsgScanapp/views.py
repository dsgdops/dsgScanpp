from django.shortcuts import render
from django.http import HttpResponse, request
from django.views.generic import ListView, TemplateView


def index(request):
    return HttpResponse("Index site")



