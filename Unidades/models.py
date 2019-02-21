#from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Unidades(models.Model):
    numeroPlaca = models.CharField(max_length=10, null=False)
    User = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    nombreUsuario = models.CharField(max_length=50, null=False)
    modeloUnidad = models.CharField(max_length=50, null=False)
    imei = models.CharField(max_length=50, null=False)
