from django.db.models import base
from django.urls import path
from rest_framework import urlpatterns
from rest_framework.routers import SimpleRouter
from .views import DeviceViewset, LogDeviceViewset, LogUserViewset, UserViewset, TypeViewset
# from django.urls import

rou = SimpleRouter()

rou.register('users', UserViewset, basename="UserViewSetEndpoint")
rou.register('types', TypeViewset, basename="UserViewSetEndpoint")
rou.register('devices', DeviceViewset, basename="DeviceViewSetEndpoint")
rou.register('devicehistory', LogDeviceViewset,
             basename="LogDeviceViewSetEndpoint")
rou.register('userhistory', LogUserViewset, basename="LogUserViewSetEndpoint")

urlpatterns = rou.urls
