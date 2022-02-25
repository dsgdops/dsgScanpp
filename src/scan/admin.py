from django.contrib import admin
from .models import scan, categorieScan, host
# Register your models here.

admin.site.register(scan)
admin.site.register(categorieScan)
admin.site.register(host)