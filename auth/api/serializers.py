from rest_framework import serializers
from django.contrib.auth.models import User
from users.models import ExtracurricularReference


class BaseSerializer(serializers.ModelSerializer):
    class Meta:
        abstract = True
        fields = '__all__'

class UserSerializer(BaseSerializer):
    class Meta(BaseSerializer.Meta):
        model = User

class UCSerializer(BaseSerializer):
    class Meta(BaseSerializer.Meta):
        model = ExtracurricularReference