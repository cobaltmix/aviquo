from django.contrib.auth.models import User
from django.db.models.fields import Field
from rest_framework import viewsets
from .serializers import UserSerializer, UCSerializer
from users.models import ExtracurricularReference
# Create your views here.

class BaseViewSet(viewsets.ModelViewSet):
    serializer_class, model, queryset = None, None, None

    def get_queryset(self):
        filter_params = {key: self.request.query_params.get(key) for key in [field.name for field in self.model._meta.get_fields()]}
        return self.model.objects.filter(**{k: v for k, v in filter_params.items() if v is not None})

    def create(self, request, *args, **kwargs):
        # Custom create logic if needed
        pass

    def update(self, request, *args, **kwargs):
        # Custom update logic if needed
        pass

class UserViewSet(BaseViewSet):
    model = User
    serializer_class = UserSerializer
    queryset = model.objects.all()


class ECSViewSet(BaseViewSet):
    model = ExtracurricularReference
    serializer_class = UCSerializer
    queryset = model.objects.all()