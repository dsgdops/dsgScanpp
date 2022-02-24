from django.shortcuts import render
from django.http import HttpResponse, request
from .models import scan
from django.views.generic import ListView, TemplateView, DetailView,FormView
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


    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        date = datetime.today().strftime('%Y-%m-%d')
        host = form.cleaned_data["host"]
        form.run_scan(host)
        q = scan(host=host, ports=form.run_scan(host), date=date)
        q.save()
        return super().form_valid(form)



class scanSuccess(TemplateView):
    template_name = 'scan/scan_success.html'



