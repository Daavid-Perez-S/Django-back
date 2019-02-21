from rest_framework import serializers
from .models import Unidades

class UnidadesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Unidades
        fields = ('numeroPlaca', 'nombreUsuario','modeloUnidad','imei')
