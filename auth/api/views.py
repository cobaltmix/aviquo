from django.shortcuts import render
from django.db.models.fields import Field
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, login

from .serializers import UserSerializer, ExtracurricularReferenceSerializer, AwardReferenceSerializer, ScholarshipReferenceSerializer, ForumSerializer
# Create your views here.
# from ..users.models import ExtracurricularReference
# from ..users.serializers import ECSSerializer
from users.models import ExtracurricularReference, AwardReference, ScholarshipReference, Forum 
from django.contrib.auth import get_user_model
User = get_user_model()

class BaseViewSet(viewsets.ModelViewSet):
    serializer_class, model, queryset = None, None, None
    def get_queryset(self):
        filter_params = {key: self.request.query_params.get(key) for key in [field.name for field in self.model._meta.get_fields()]}
        return self.model.objects.filter(**{k: v for k, v in filter_params.items() if v is not None})

class UserRegistrationView(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            user = User.objects.get(username=serializer.data['username'])
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'token': token.key})
        return Response(serializer.errors, status=400)

class UserLoginView(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'token': token.key})
        return Response({'detail': 'Invalid credentials'}, status=401)

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

class ForumViewSet(BaseViewSet):
    model = Forum
    serializer_class = ForumSerializer
    queryset = model.objects.all()