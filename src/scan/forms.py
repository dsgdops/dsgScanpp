from django import forms
from .models import categorieScan
import nmap

class addscanForm(forms.Form):
    host = forms.CharField()
    categorie = forms.ModelChoiceField(queryset=categorieScan.objects.all().order_by('nom'), initial="Catégorie")

    def run_scan(self, host):
        nm = nmap.PortScanner()
        nm.scan(host, '22-443')
        port = nm[host]['tcp']
        return port


