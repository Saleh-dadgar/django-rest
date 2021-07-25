from django.contrib.auth import get_user_model
from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated

from django_rest.models import Articel
from .permissions import IsSuperUser, IsStaffOrReadOnly, IsAuthorOrReadOnly, IsSuperUserOrStaffReadOnly
from .serializers import ArticelSerializers, UserSerializer
from rest_framework.generics import ListCreateAPIView
from rest_framework.viewsets import ModelViewSet


# Create your views here.


class ArticleViewSet(ModelViewSet):
    queryset =  Articel.objects.all()
    serializer_class = ArticelSerializers
    filterset_fields =['status', 'auther__username']
    ordering_fields=['status','publish']
    search_fields=['title','auther__username','content']

    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.action in ['list', 'create']:
            permission_classes = [IsStaffOrReadOnly]
        else:
            permission_classes = [IsAuthorOrReadOnly, IsStaffOrReadOnly]
        return [permission() for permission in permission_classes]



class UserViewSet(ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsSuperUserOrStaffReadOnly,)