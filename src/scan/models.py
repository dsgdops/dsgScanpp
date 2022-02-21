from django.db import models

# Create your models here.
class scans(models.Model):
    host = models.CharField(max_length=200)
    ports = models.IntegerField()
    date = models.DateField()