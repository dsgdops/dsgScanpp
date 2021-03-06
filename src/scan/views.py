from .models import scan, categorieScan, host, hostScan
from django.views.generic import ListView, TemplateView, DetailView,FormView, CreateView, DeleteView
from .forms import addscanForm
from datetime import datetime
from django.urls import reverse, reverse_lazy
from django.shortcuts import render

class scanHistory(ListView):
    template_name = 'scan/scan_history.html'
    context_object_name = 'scan_list'
    def get_queryset(self):
        """Return the last five scans."""
        return scan.objects.order_by('-date')[:5]

class scanDetails(DetailView):
    model = hostScan
    template_name = 'scan/scan_details.html'

    def get_object(self, queryset=None):
        return hostScan.objects.filter(scan_id=self.kwargs.get("uuid"))

class scanConfiguration(FormView):
    template_name = 'scan/scan_configuration.html'
    form_class = addscanForm
    model = categorieScan

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the categorie
        context['categorie_list'] = categorieScan.objects.all()
        return context

    def get_success_url(self):
        return reverse_lazy('scan_history')

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        date = datetime.today().strftime('%Y-%m-%d')
        categorie = form.cleaned_data["categorie"]

        all_host_categorie = host.objects.filter(categorie=categorie)
        q = scan(categorie=categorie, date=date)
        q.save()
        for ip in all_host_categorie:
            ip = str(ip)
            print("Scan de ", ip, " en cours...")
            q2 = hostScan(scan_id=q ,host=ip, ports=form.run_scan(ip), portsUDP=form.run_scanUDP(ip))
            q2.save()
        return super().form_valid(form)

class categorieConfiguration(CreateView):
    template_name = 'scan/categorie_configuration.html'
    model = categorieScan
    fields = ['nom']

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['categorie_list'] = categorieScan.objects.all()
        return context

    def get_success_url(self):
        return self.request.path

class configurationIndex(TemplateView):
    template_name = 'scan/configuration_index.html'

class categorieSettings(TemplateView):
    template_name = 'scan/categorie_settings.html'

class listHost(ListView):
    template_name = 'scan/list_host.html'
    context_object_name = 'host_list'
    def get_queryset(self):
        """Return the last five scans."""
        return host.objects.order_by('host')

class categorieAddHost(CreateView):
    template_name = 'scan/categorie_add-host.html'
    model = host
    fields = ['host', 'categorie']

    def get_success_url(self):
        return self.request.path

class scanDelete(DeleteView):
    model = scan
    success_url = reverse_lazy('scan_history')

    def get_success_url(self):
        return reverse("scan_history")

class hostDelete(DeleteView):
    model = host
    success_url = reverse_lazy('list_host')

    def get_success_url(self):
        return reverse("list_host")

class listCategorie(ListView):
    template_name = 'scan/list_categorie.html'
    context_object_name = 'categorie_list'
    def get_queryset(self):
        """Return the last five categorie."""
        return categorieScan.objects.order_by('nom')

class categorieDelete(DeleteView):
    model = categorieScan
    success_url = reverse_lazy('categorie_settings')

    def get_success_url(self):
        return reverse("categorie_settings")


def error404(request, exception):
    return render(request,'404.html')


def error500(request):
    return render(request,'500.html')