from django.contrib import admin
from .models import scan, categorieScan, host, hostScan
# Register your models here.

admin.site.register(scan)
admin.site.register(categorieScan)
admin.site.register(host)
admin.site.register(hostScan)
