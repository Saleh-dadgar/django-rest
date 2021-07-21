from django.urls import path

from .views import Articel_list,ArticelDetail,UserList,UserDetail
app_name= 'api'
urlpatterns = [
    path('',Articel_list.as_view(),name='list'),
    path('users/',UserList.as_view(),name='list'),
    path('<int:pk>',ArticelDetail.as_view(),name='detail'),
    path('users/<int:pk>',UserDetail.as_view(),name='detail'),


]
