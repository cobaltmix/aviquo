from django.shortcuts import render
from django.contrib.auth.models import User
from django.db.models.fields import Field
from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import UserSerializer
# Create your views here.
# from ..users.models import ExtracurricularReference
# from ..users.serializers import ECSSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_queryset(self):
        #aggregate query params
        filter_params = {key: self.request.query_params.get(key) for key in [field.name for field in User._meta.get_fields()]}

        #eliminate nonexistent params & filter from model
        return User.objects.filter(**{k: v for k, v in filter_params.items() if v is not None})



