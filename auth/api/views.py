from django.shortcuts import render
from django.contrib.auth.models import User
from django.db.models.fields import Field
from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import UserSerializer, ExtracurricularReferenceSerializer, AwardReferenceSerializer, ScholarshipReferenceSerializer
# Create your views here.
# from ..users.models import ExtracurricularReference
# from ..users.serializers import ECSSerializer
from auth.users.models import ExtracurricularReference, AwardReference, ScholarshipReference


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_queryset(self):
        #aggregate query params
        filter_params = {key: self.request.query_params.get(key) for key in [field.name for field in User._meta.get_fields()]}

        #eliminate nonexistent params & filter from model
        return User.objects.filter(**{k: v for k, v in filter_params.items() if v is not None})



class ECSListView(viewsets.ModelViewSet):
    queryset = ExtracurricularReference.objects.all()
    serializer_class = ExtracurricularReferenceSerializer

    def get_queryset(self):
        # aggregate query params
        filter_params = {key: self.request.query_params.get(key) for key in
                         [field.name for field in ExtracurricularReference._meta.get_fields()]}

        # eliminate nonexistent params & filter from model
        return ExtracurricularReference.objects.filter(**{k: v for k, v in filter_params.items() if v is not None})


# class AWSCreateView(generics.CreateAPIView):
#     queryset = AwardReference.objects.all()
#     serializer_class = AWSSerializer


class AWSListView(viewsets.ModelViewSet):
    queryset = AwardReference.objects.all()
    serializer_class = AwardReferenceSerializer

    def get_queryset(self):
        # aggregate query params
        filter_params = {key: self.request.query_params.get(key) for key in
                         [field.name for field in AwardReference._meta.get_fields()]}

        # eliminate nonexistent params & filter from model
        return AwardReference.objects.filter(**{k: v for k, v in filter_params.items() if v is not None})


# class SCCreateView(generics.CreateAPIView):
#     queryset = ScholarshipReference.objects.all()
#     serializer_class = SCSerializer


class SCCListView(viewsets.ModelViewSet):
    queryset = ScholarshipReference.objects.all()
    serializer_class = ScholarshipReferenceSerializer

    def get_queryset(self):
        # aggregate query params
        filter_params = {key: self.request.query_params.get(key) for key in
                         [field.name for field in ScholarshipReference._meta.get_fields()]}

        # eliminate nonexistent params & filter from model
        return ScholarshipReference.objects.filter(**{k: v for k, v in filter_params.items() if v is not None})