from rest_framework import serializers
from .models import Forum, Opportunity, User, Waitlist


class ForumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Forum
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class OpportunitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Opportunity
        fields = "__all__"


class WaitlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Waitlist
        fields = "__all__"
