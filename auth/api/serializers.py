from rest_framework import serializers
from django.contrib.auth.models import User
from users.models import ExtracurricularReference, AwardReference

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class UCSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExtracurricularReference
        fields = '__all__'