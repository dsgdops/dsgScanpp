from django import forms
import nmap

class addscanForm(forms.Form):
    host = forms.CharField()

    def run_scan(self, host):
        nm = nmap.PortScanner()
        nm.scan(host, '22-443')
        port = nm[host]['tcp']
        return port