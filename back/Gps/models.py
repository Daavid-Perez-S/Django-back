from __future__ import unicode_literals
from django.db import models

# Create your models here.

class Gps(models.Model):
    latitudGps = models.CharField(max_length=50, null=False)
    longitudGps = models.CharField(max_length=50, null=False)
    fechaGps = models.DateField(null=False)
    horaGps = models.TimeField(null=False)
    imei = models.CharField(max_length=50, null=False)
