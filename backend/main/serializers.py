from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Forum, Opportunity, Waitlist
<<<<<<< HEAD:backend/users/serializers.py
# from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
# User = get_user_model()
=======

>>>>>>> 36f805169e405883de6a3ee8e8612efb2ae3b20c:backend/main/serializers.py

class ForumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Forum
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = "__all__"


class OpportunitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Opportunity
        fields = "__all__"


class WaitlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Waitlist
        fields = "__all__"
