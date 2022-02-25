from django.shortcuts import render
from django.http import HttpResponse, request
from .models import scan, categorieScan
from django.views.generic import ListView, TemplateView, DetailView,FormView, CreateView
from . import script
from .forms import addscanForm
from datetime import datetime


class scanHistory(ListView):
    template_name = 'scan/scan_history.html'
    context_object_name = 'scan_list'
    def get_queryset(self):
        """Return the last five scans."""
        return scan.objects.order_by('-date')[:5]

class scanDetails(DetailView):
    model = scan
    template_name = 'scan/scan_details.html'

    def get_object(self, queryset=None):
        return scan.objects.get(scan_id=self.kwargs.get("uuid"))

class scanConfiguration(FormView):
    template_name = 'scan/scan_configuration.html'
    success_url = 'success/'
    form_class = addscanForm
    model = categorieScan

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['categorie_list'] = categorieScan.objects.all()
        return context


    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        date = datetime.today().strftime('%Y-%m-%d')
        host = form.cleaned_data["host"]
        categorie = form.cleaned_data["categorie"]

        form.run_scan(host)
        q = scan(host=host,categorie=categorie, ports=form.run_scan(host), date=date)
        q.save()
        return super().form_valid(form)

class scanSuccess(TemplateView):
    template_name = 'scan/scan_success.html'

class categorieConfiguration(CreateView):
    template_name = 'scan/categorie_configuration.html'
    model = categorieScan
    fields = ['nom']
