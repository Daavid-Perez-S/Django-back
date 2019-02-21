#from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):

    User = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    estado = models.CharField(max_length=50, null=False)
    descripcion = models.CharField(max_length=10, null=False)
