from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Gps(models.Model):
    User = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    latitudGps = models.CharField(max_length=50, null=False)
    longitudGps = models.CharField(max_length=50, null=False)
    fechaGps = models.DateField(null=False)
    horaGps = models.TimeField(null=False)
    imei = models.CharField(max_length=50, null=False)
