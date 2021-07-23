from django.urls import path, include
from rest_framework import routers
from .views import UserViewSet,ArticelSet

app_name= 'api'

router = routers.SimpleRouter()
router.register('', ArticelSet)
router.register('users', UserViewSet)




urlpatterns = [

    path('', include(router.urls))

]
