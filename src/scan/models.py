import uuid

from django.db import models
import random

# Create your models here.


class categorieScan(models.Model):
    id = models.BigAutoField(primary_key=True)
    nom = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.nom


class scan(models.Model):
    scan_id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4,editable=False)
    host = models.GenericIPAddressField()
    ports = models.JSONField()
    date = models.DateField()
    categorie = models.ForeignKey(categorieScan,null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.host


class host(models.Model):
    id = models.BigAutoField(primary_key=True)
    host = models.GenericIPAddressField()
    categorie = models.ForeignKey(categorieScan,null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.host