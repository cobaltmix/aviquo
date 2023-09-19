from rest_framework import serializers
from .models import ExtracurricularReference

class ECSSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExtracurricularReference
        fields = '__all__'