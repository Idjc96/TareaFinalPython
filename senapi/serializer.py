from rest_framework import serializers
from .models import Senapi

class SenapiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Senapi
        fields = '__all__'