from rest_framework import serializers
from django.contrib.auth.models import User

from auth.users.models import ExtracurricularReference, AwardReference, ScholarshipReference


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class ExtracurricularReferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExtracurricularReference
        fields = '__all__'

class AwardReferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = AwardReference
        fields = '__all__'

class ScholarshipReferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScholarshipReference
        fields = '__all__'
