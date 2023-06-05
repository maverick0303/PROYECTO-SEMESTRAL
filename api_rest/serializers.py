from rest_framework import serializers
from tiendita.models import Region, Comuna

class comunaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Comuna
        fields = ['id_comuna', 'nombre', 'region']

class regionSerializers(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ['id_region', 'nombre']