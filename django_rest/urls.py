
from django.urls import path

from django_rest.views import Articel_list, ArticelDetail

app_name= 'django_rest'
urlpatterns = [
    path('',Articel_list.as_view(),name='list'),
    path('<int:pk>',ArticelDetail.as_view(),name='detail'),

]
