from rest_framework import serializers
from .models import Planta, Producto, RegistroProduccion

class PlantaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Planta
        fields = ['codigo', 'nombre']

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ['codigo', 'nombre', 'planta']

class RegistroProduccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegistroProduccion
        fields = ['producto', 'litros', 'fecha_produccion', 'turno', 'hora_registro', 'operador']
