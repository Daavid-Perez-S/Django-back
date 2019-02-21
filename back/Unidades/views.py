from django.shortcuts import get_object_or_404
from rest_framework import generics
from .models import Unidades
from .serializers import UnidadesSerializer

# Create your views here.

class UnidadesList(generics.ListCreateAPIView):
    queryset = Unidades.objects.all()
    serializer_class = UnidadesSerializer

    # Función para traer los objetos
    def get_object(self):
        # Método para traer los objetos de Profile
        queryset = self.get_queryset()
        # Nos trae el objeto o un error de 404, de que no lo encontró
        obj = get_object_or_404(
            queryset,
            pk=self.kwargs['pk'],
        )
        return obj
