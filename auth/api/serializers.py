from rest_framework import serializers

from django.contrib.auth.models import User
from users.models import ExtracurricularReference, AwardReference, ScholarshipReference, Forum


class BaseSerializer(serializers.ModelSerializer):
    class Meta:
        abstract = True
        fields = '__all__'

class UserSerializer(BaseSerializer):
    class Meta(BaseSerializer.Meta):
        model = User



class ExtracurricularReferenceSerializer(BaseSerializer):
    class Meta(BaseSerializer.Meta):
        model = ExtracurricularReference


class AwardReferenceSerializer(BaseSerializer):
    class Meta(BaseSerializer.Meta):
        model = AwardReference


class ScholarshipReferenceSerializer(BaseSerializer):
    class Meta(BaseSerializer.Meta):
        model = ScholarshipReference

class ForumSerializer(BaseSerializer):
    class Meta(BaseSerializer.Meta):
        model = Forum
