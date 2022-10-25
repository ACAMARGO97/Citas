from rest_framework import serializers
from apps.factura.models import *

class FacturaSerializer(serializers.ModelSerializer):
    class Meta:
        model=Factura
        fields=('__all__')

class AgendaSerializer(serializers.ModelSerializer):
    class Meta:
        model= Agenda
        fields=('__all__')