from django.shortcuts import get_object_or_404
from rest_framework import generics
from .models import Register
from .serializers import RegisterSerializer

# Create your views here.

class RegisterList(generics.ListCreateAPIView):
    queryset = Register.objects.all()
    serializer_class = RegisterSerializer

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
