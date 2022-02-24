import uuid

from django.db import models
import random

# Create your models here.
class scan(models.Model):
    scan_id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4,editable=False)
    host = models.GenericIPAddressField()
    ports = models.JSONField()
    date = models.DateField()

    def __str__(self):
        return self.host