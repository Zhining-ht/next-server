from rest_framework.viewsets import ModelViewSet
from django.contrib.auth.models import User
from .serializer import UserListSerializer
from ...viewsets import ModelViewSetWithCustomResponse


class UserListView(ModelViewSetWithCustomResponse):
    queryset = User.objects.all()
    serializer_class = UserListSerializer


from django.contrib.auth.models import User
from rest_framework.renderers import BrowsableAPIRenderer
from rest_framework.viewsets import ModelViewSet
from .serializer import UserListSerializer
from ...renders import SuccessAPIRenderer


class UserListView(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserListSerializer
    lookup_field = 'username'
    renderer_classes = [SuccessAPIRenderer, BrowsableAPIRenderer]
