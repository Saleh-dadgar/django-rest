from django.contrib.auth import get_user_model
from rest_framework import serializers

from django_rest.models import Articel


class ArticelSerializers(serializers.ModelSerializer):
    class Meta:
        model = Articel
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = "__all__"
