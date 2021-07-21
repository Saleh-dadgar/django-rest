from django.contrib.auth.models import User
from django.shortcuts import render

from django_rest.models import Articel
from .permissions import IsSuperUser, IsStaffOrReadOnly, IsAuthorOrReadOnly, IsSuperUserOrStaffReadOnly
from .serializers import ArticelSerializers, UserSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView, DestroyAPIView


# Create your views here.

class Articel_list(ListCreateAPIView, DestroyAPIView):
    queryset = Articel.objects.all()
    serializer_class = ArticelSerializers


class ArticelDetail(RetrieveAPIView, DestroyAPIView):
    queryset = Articel.objects.all()
    serializer_class = ArticelSerializers
    permission_classes = (IsAuthorOrReadOnly, IsStaffOrReadOnly)


class UserList(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsSuperUserOrStaffReadOnly,)


class UserDetail(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsSuperUserOrStaffReadOnly,)

