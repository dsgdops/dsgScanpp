from django.db import models

# Create your models here.
class scan(models.Model):
    host = models.GenericIPAddressField()
    ports = models.JSONField()
    date = models.DateField()

    def __str__(self):
        return self.host