import random

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
# from ..users.models import ExtracurricularReference
# from ..users.serializers import ECSSerializer
from main.models import Forum, Opportunity, Tag, User, Waitlist
from rest_framework import generics, permissions, viewsets
from rest_framework_api_key.models import APIKey

from .serializers import ForumSerializer, OpportunitySerializer, TagSerializer, UserSerializer, WaitlistSerializer


class BaseViewSet(viewsets.ModelViewSet):
    serializer_class, model, queryset = None, None, None

    def get_queryset(self):
        filter_params = {
            key: self.request.query_params.get(key) for key in [field.name for field in self.model._meta.get_fields()]
        }
        return self.model.objects.filter(**{k: v for k, v in filter_params.items() if v is not None})


class UserViewSet(BaseViewSet):
    model = User
    serializer_class = UserSerializer
    queryset = model.objects.all()


class RegistrationAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.AllowAny,)


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
    if request.headers.get("Referer") == "http://localhost:3000/":
        name = "demo-key-gen-" + str(random.randint(100, 20000))

        _, key = APIKey.objects.create_key(name=name)
        response_data = {"key": key}

        return JsonResponse(response_data)
    else:
        return JsonResponse({"error": "Unauthorized"}, status=401)
