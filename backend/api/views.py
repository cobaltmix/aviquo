from django.shortcuts import render
from django.db.models.fields import Field
from django.contrib.auth.models import User
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, login
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.views import APIView
from .serializers import UserSerializer, ForumSerializer, OpportunitySerializer, TagSerializer, LoginSerializer, WaitlistSerializer
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework_api_key.models import APIKey
import random
# Create your views here.
# from ..users.models import ExtracurricularReference
# from ..users.serializers import ECSSerializer
from users.models import Forum, Opportunity, Tag, Waitlist
from django.contrib.auth import get_user_model
User = get_user_model()

class BaseViewSet(viewsets.ModelViewSet):
    serializer_class, model, queryset = None, None, None
    def get_queryset(self):
        filter_params = {key: self.request.query_params.get(key) for key in [field.name for field in self.model._meta.get_fields()]}
        return self.model.objects.filter(**{k: v for k, v in filter_params.items() if v is not None})



class UserViewSet(BaseViewSet):
    model = User
    serializer_class = UserSerializer
    queryset = model.objects.all()

class RegistrationAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.AllowAny,)

# Use TokenObtainPairView for login
class LoginAPIView(TokenObtainPairView):
    serializer_class = LoginSerializer

# Use TokenRefreshView for token refresh
class TokenRefreshAPIView(TokenRefreshView):
    pass


class ForumViewSet(BaseViewSet):
    model = Forum
    serializer_class = ForumSerializer
    queryset = model.objects.all()

class OpportunityViewSet(BaseViewSet):
    model = Opportunity
    serializer_class = OpportunitySerializer
    queryset = model.objects.all()

class TagViewSet(BaseViewSet):
    model = Tag
    serializer_class = TagSerializer
    queryset = model.objects.all()
class WaitlistViewSet(BaseViewSet):
    model = Waitlist
    serializer_class = WaitlistSerializer
    queryset = model.objects.all()
    
@csrf_exempt  
def gen_api_key(request):
    if request.headers.get('Referer') == 'http://localhost:3000/':
        name = "demo-key-gen-" + str(random.randint(100, 20000))

        _, key = APIKey.objects.create_key(name=name)
        response_data = { 'key' : key }

        return JsonResponse(response_data)
    else:
        return JsonResponse({'error': 'Unauthorized'}, status=401)