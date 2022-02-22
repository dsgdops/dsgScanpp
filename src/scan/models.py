from django.db import models

# Create your models here.
class scan(models.Model):
    host = models.CharField(max_length=200)
    ports = models.CharField(max_length=200)
    date = models.DateField()

    def __str__(self):
        return self.host