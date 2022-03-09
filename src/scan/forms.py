from django import forms
from .models import categorieScan
from . import nmap

class addscanForm(forms.Form):
    categorie = forms.ModelChoiceField(queryset=categorieScan.objects.all().order_by('nom'), initial="Catégorie")

    def run_scan(self, host):
        nm = nmap.PortScanner()
        nm.scan(host, '22-443', '-v -sS')
        port = nm[host]['tcp']

        return port

    def run_scanUDP(self, host):
        nm = nmap.PortScanner()
        nm.scan(host, '1-1024', '-v -sU')
        portUDP = nm[host]['udp']

        return portUDP