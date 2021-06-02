from rest_framework.fields import NullBooleanField
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework import pagination
from deviceapp.permissions import LogPermissions, LogRetrivePermissions
from deviceapp.models import Device, Type
from django.contrib.auth.models import User
from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework import generics, views, viewsets, filters
from rest_framework.decorators import action
from .serializers import *
# Create your views here.


class MyPagination(pagination.PageNumberPagination):
    page_size_query_param = 'limit'


def addUserLog(request, obj_instance):
    if request == 'POST':
        temp = LogUser(logTitle="User created", logUser=obj_instance)
        temp.save()
    elif request == 'PATCH':
        temp = LogUser(logTitle="User partially updated.",
                       logUser=obj_instance)
        temp.save()
    elif request == 'PUT':
        temp = LogUser(logTitle="User updated.", logUser=obj_instance)
        temp.save()
    elif request == 'alloc':
        temp = LogUser(logTitle="New Device allocated",
                       logUser=obj_instance)
        temp.save()
    elif request == 'dealloc':
        temp = LogUser(logTitle="Device Deallocated.",
                       logUser=obj_instance)
        temp.save()
    elif request == 'swap':
        temp = LogUser(logTitle="User swapped with new device.",
                       logUser=obj_instance)
        temp.save()


def addDeviceLog(request, obj_instance):
    if request == 'POST':
        temp = LogDevice(logTitle="Device created", logDevice=obj_instance)
        temp.save()
    elif request == 'PATCH':
        temp = LogDevice(logTitle="Device partially updated.",
                         logDevice=obj_instance)
        temp.save()
    elif request == 'PUT':
        temp = LogDevice(logTitle="Device updated.", logDevice=obj_instance)
        temp.save()
    elif request == 'alloc':
        temp = LogDevice(logTitle="User added", logDevice=obj_instance)
        temp.save()
    elif request == 'dealloc':
        temp = LogDevice(logTitle="User removed", logDevice=obj_instance)
        temp.save()
    elif request == 'swap':
        temp = LogDevice(
            logTitle="Device Swapped with new user.", logDevice=obj_instance)
        temp.save()


class UserViewset(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    pagination_class = MyPagination

    def perform_create(self, serializer):
        id = serializer.save()
        addUserLog('POST', id)

    def update(self, request, *args, **kwargs):
        inst = self.get_object()
        addUserLog('PUT', inst)
        return super().update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        inst = self.get_object()
        addUserLog('PATCH', inst)
        return super().partial_update(request, *args, **kwargs)

    @action(
        methods=['GET'],
        detail=True,
        permission_classes=[IsAuthenticatedOrReadOnly],
        url_path='history',
        url_name='history'
    )
    def User_History(self, request, *args, **kwargs):
        self.serializer_class = UserRetireveSerializer
        return viewsets.ModelViewSet.retrieve(self, request, *args, **kwargs)

    @action(
        methods=['GET'],
        detail=False,
        permission_classes=[IsAuthenticatedOrReadOnly],
        url_path='search',
        url_name='Device-search'
    )
    def Search_User(self, request, *args, **kwargs):
        self.search_fields = ['username', 'email']
        self.filter_backends = (filters.SearchFilter,)
        self.queryset = get_user_model().objects.all()
        self.serializer_class = UserSerializer
        return viewsets.ModelViewSet.list(self, request, *args, **kwargs)

    @action(
        methods=['GET', 'PATCH'],
        detail=False,
        permission_classes=[IsAuthenticatedOrReadOnly],
        url_path='swapdevice',
        url_name='Swap-Device'
    )
    def swap_device(self, request, *args, **kwargs):

        user1_id = request.data['user1_id']
        device1_id = request.data['device1_id']
        device2_id = request.data['device2_id']
        user2_id = request.data['user2_id']

        res = Response()
        if not (user1_id and user2_id and device1_id and device2_id):
            res.status_code = 400
            res.data = "{Error: Bad request.}"
            return res

        device1 = Device.objects.get(id=device1_id)
        device2 = Device.objects.get(id=device2_id)
        user1 = get_user_model().objects.get(id=user1_id)
        user2 = get_user_model().objects.get(id=user2_id)

        if not (user1 and user2 and device1 and device2) or device1.deviceUser != user1 or device2.deviceUser != user2:
            res.status_code = 400
            res.data = "{Error: User-Device pair not found. }"
            return res

        device1.deviceUser = user2
        device2.deviceUser = user1
        device1.save()
        device2.save()

        addDeviceLog("swap", device1)
        addDeviceLog("swap", device2)
        addUserLog("swap", user1)
        addUserLog("swap", user2)

        res.status_code = 200
        res.data = " Success: Device swapped among users."
        return res


class TypeViewset(viewsets.ModelViewSet):
    permission_classes = (LogRetrivePermissions, IsAuthenticatedOrReadOnly,)
    queryset = Type.objects.all()
    serializer_class = TypeSerializer

    def retrieve(self, request, *args, **kwargs):
        self.serializer_class = Type_Retrieve_Serializer
        return viewsets.ModelViewSet.retrieve(self, request, *args, **kwargs)


class DeviceViewset(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
    pagination_class = MyPagination

    def perform_create(self, serializer):
        id = serializer.save()
        addDeviceLog('POST', id)

    def update(self, request, *args, **kwargs):
        inst = self.get_object()
        addDeviceLog('PUT', inst)
        return super().update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        inst = self.get_object()
        addDeviceLog('PATCH', inst)
        return super().partial_update(request, *args, **kwargs)

    @action(
        methods=['GET'],
        detail=True,
        url_path='history',
        url_name='history'
    )
    def Device_History(self, request, *args, **kwargs):
        self.serializer_class = DeviceHistorySerializer
        return viewsets.ModelViewSet.retrieve(self, request, *args, **kwargs)

    @action(
        methods=['GET'],
        detail=False,
        url_path='search',
        url_name='Device-search'
    )
    def search_device(self, request, *args, **kwargs):
        self.search_fields = ['deviceName', 'deviceType__typeName']
        self.filter_backends = (filters.SearchFilter,)
        self.queryset = Device.objects.all()
        self.serializer_class = DeviceSerializer
        return viewsets.ModelViewSet.list(self, request, *args, **kwargs)

    @action(
        methods=['PATCH'],
        detail=True,
        url_path='allocate',
        url_name='Allocate Device'
    )
    def device_allocate(self, request, *args, **kwargs):
        res = Response()

        device = self.get_object()
        user_id = request.data['user_id']

        if device.deviceUser or not user_id:
            res.status_code = 400
            if device.deviceUser:
                res.data = " { Error: Device allready allocated. }"
            else:
                res.data = " { Error: User_id not found. }"
            return res
        user = get_user_model().objects.get(id=user_id)

        addDeviceLog("alloc", device)
        addUserLog("alloc", user)

        device.deviceUser = user
        device.save()

        res.data = DeviceSerializer(self.get_object()).data
        res.status_code = 200
        return res

    @action(
        methods=['PATCH'],
        detail=True,
        url_path='deallocate',
        url_name='Deallocate Device'
    )
    def device_Deallocate(self, request, *args, **kwargs):
        res = Response()

        device = self.get_object()
        if not device.deviceUser:
            res.status_code = 400
            res.data = " { Error: Device allready deallocated. }"
            return res

        addDeviceLog("dealloc", device)
        addUserLog("dealloc", device.deviceUser)

        device.deviceUser = None
        device.save()

        res.data = DeviceSerializer(self.get_object()).data
        res.status_code = 200
        return res


class LogDeviceViewset(viewsets.ModelViewSet):
    permission_classes = (
        LogPermissions, LogRetrivePermissions, IsAuthenticatedOrReadOnly, )
    queryset = LogDevice.objects.all()
    serializer_class = DeviceLogSerializer

    def get_queryset(self):
        queryset = self.queryset.order_by('-logTime')
        return queryset


class LogUserViewset(viewsets.ModelViewSet):
    permission_classes = (
        LogPermissions, LogRetrivePermissions, IsAuthenticatedOrReadOnly, )
    queryset = LogUser.objects.all()
    serializer_class = UserLogSerializer

    def get_queryset(self):
        queryset = self.queryset.order_by('-logTime')
        return queryset
