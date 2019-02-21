from rest_framework import serializers
from .models import Register

class RegisterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Register
        fields = ('nombreUsuario', 'apellidosUsuario','edadUsuario','correoUsuario','fechaNacimientoUsuario','sexo','password')
