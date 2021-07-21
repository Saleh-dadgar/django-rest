from django.contrib.auth.models import User
from django.db import models


# Create your models here.
from django.utils import timezone


class Articel(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    auther=models.ForeignKey(User, on_delete=models.CASCADE)
    content=models.TextField(max_length=500)
    created=models.DateTimeField(auto_now_add=True)
    publish=models.DateTimeField(default=timezone.now)
    updete=models.DateTimeField(auto_now=True)
    status=models.BooleanField(default=False)


    def __str__(self):
        return self.title