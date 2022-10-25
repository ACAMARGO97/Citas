from rest_framework import serializers
from apps.personas.models import *

class PersonasSerializer(serializers.ModelSerializer):
    class Meta:
        model=Personas
        fields=('__all__')

class EmpleadoSerializer(serializers.ModelSerializer):
    class Meta:
        model= Empleado
        fields=('__all__')

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model=Cliente
        fields=('__all__')