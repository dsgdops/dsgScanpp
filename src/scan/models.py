from django.db import models
import random

# Create your models here.
class scan(models.Model):
    scan_id = models.BigAutoField(primary_key=True)
    host = models.GenericIPAddressField()
    ports = models.JSONField()
    date = models.DateField()

    def __str__(self):
        return self.host