from rest_framework import serializers

from django.contrib.auth.models import User
from users.models import  Forum, Opportunity, Tag, Waitlist
from django.contrib.auth import get_user_model
User = get_user_model()

class BaseSerializer(serializers.ModelSerializer):
    class Meta:
        abstract = True
        fields = '__all__'



class UserSerializer(BaseSerializer):
    class Meta(BaseSerializer.Meta):
        model = User
        # fields = ('id', 'username', 'email', 'password')
        # extra_kwargs = {'password': {'write_only': True}}

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
        
class ForumSerializer(BaseSerializer):
    class Meta(BaseSerializer.Meta):
        model = Forum

class OpportunitySerializer(BaseSerializer):
    class Meta(BaseSerializer.Meta):
        model = Opportunity
        
class TagSerializer(BaseSerializer):
    class Meta(BaseSerializer.Meta):
        model = Tag

class WaitlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Waitlist
        fields = '__all__'
