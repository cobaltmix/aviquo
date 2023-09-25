from rest_framework import serializers
from .models import ExtracurricularReference, AwardReference, ScholarshipReference, Forum
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
User = get_user_model()
class ForumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Forum
        fields = '__all__'

class ECSSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExtracurricularReference
        fields = '__all__'

class AWSSerializer(serializers.ModelSerializer):
    class Meta:
        model = AwardReference
        fields = '__all__'

class SCSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScholarshipReference
        fields = '__all__'
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'