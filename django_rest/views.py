from django.shortcuts import render , get_object_or_404

# Create your views here.
from django.views.generic import ListView, DetailView

from django_rest.models import Articel


class Articel_list(ListView):
    def get_queryset(self):
        return Articel.objects.filter(status=True)


class ArticelDetail(DetailView):
    def get_object(self):
        return get_object_or_404(Articel.objects.filter(status=True),pk=self.kwargs.get('pk'))
