from rest_framework import serializers
from .models import Gps

class GpsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Gps
        fields = ('latitudGps', 'longitudGps', 'fechaGps', 'horaGps', 'imei')
