from rest_framework import serializers
from .models import Deportista


class DeportistaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deportista
        fields = '__all__'
