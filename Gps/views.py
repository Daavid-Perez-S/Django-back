from django.shortcuts import get_object_or_404
from rest_framework import generics
from .models import Gps
from .serializers import GpsSerializer

# Create your views here.

class GpsList(generics.ListCreateAPIView):
    queryset = Gps.objects.all()
    serializer_class = GpsSerializer

    # Función para traer los objetos
    def get_object(self):
        # Método para traer los objetos de Gps
        queryset = self.get_queryset()
        # Nos trae el objeto o un error de 404, de que no lo encontró
        obj = get_object_or_404(
            queryset,
            pk=self.kwargs['pk'],
        )
        return obj
