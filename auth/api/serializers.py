from rest_framework import serializers
from django.contrib.auth.models import User

from users.models import ExtracurricularReference, AwardReference, ScholarshipReference


class BaseSerializer(serializers.ModelSerializer):
    class Meta:
        abstract = True
        fields = '__all__'

class UserSerializer(BaseSerializer):
    class Meta:
        model = User
        fields = '__all__'


class ExtracurricularReferenceSerializer(BaseSerializer):
    class Meta:
        model = ExtracurricularReference
        fields = '__all__'

class AwardReferenceSerializer(BaseSerializer):
    class Meta:
        model = AwardReference
        fields = '__all__'

class ScholarshipReferenceSerializer(BaseSerializer):
    class Meta:
        model = ScholarshipReference
        fields = '__all__'
