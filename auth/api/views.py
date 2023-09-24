from django.shortcuts import render
from django.contrib.auth.models import User
from django.db.models.fields import Field
from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import UserSerializer, ExtracurricularReferenceSerializer, AwardReferenceSerializer, ScholarshipReferenceSerializer
# Create your views here.
# from ..users.models import ExtracurricularReference
# from ..users.serializers import ECSSerializer
from users.models import ExtracurricularReference, AwardReference, ScholarshipReference

class BaseViewSet(viewsets.ModelViewSet):
    serializer_class, model, queryset = None, None, None
    def get_queryset(self):
        filter_params = {key: self.request.query_params.get(key) for key in [field.name for field in self.model._meta.get_fields()]}
        return self.model.objects.filter(**{k: v for k, v in filter_params.items() if v is not None})

   

class UserViewSet(BaseViewSet):
    model = User
    serializer_class = UserSerializer
    queryset = model.objects.all()


class ECSViewSet(BaseViewSet):
    model = ExtracurricularReference
    serializer_class = ExtracurricularReferenceSerializer
    queryset = model.objects.all()


class AWSViewSet(BaseViewSet):
    model = AwardReference
    serializer_class = AwardReferenceSerializer
    queryset = model.objects.all()

class SCViewSet(BaseViewSet):
    model = ScholarshipReference
    serializer_class = ScholarshipReferenceSerializer
    queryset = model.objects.all()
