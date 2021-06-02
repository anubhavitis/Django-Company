from re import A
from django.db.models import fields
from deviceapp.models import Type, LogDevice, LogUser, Device
from rest_framework import serializers
from django.contrib.auth import get_user_model


class HistoryUser(serializers.ModelSerializer):
    class Meta:
        fields = ['logTitle', 'logTime']
        model = LogUser


class UserDeviceSerializer(serializers.ModelSerializer):
    deviceType = serializers.SerializerMethodField()

    def get_deviceType(self, obj):
        return obj.deviceType.typeName

    class Meta:
        model = Device
        fields = ['id', 'deviceName', 'deviceType']


class UserRetireveSerializer(serializers.ModelSerializer):
    device = UserDeviceSerializer(read_only=True, many=True)
    history = HistoryUser(read_only=True, many=True)

    class Meta:
        fields = ['id', 'username', 'device', 'email', 'history']
        model = get_user_model()


class SwapSerializer(serializers.ModelSerializer):
    device = UserDeviceSerializer(read_only=True, many=True)

    class Meta:
        fields = ['id', 'username', 'device']
        model = get_user_model()

    def __init__(self, *args, **kwargs):
        super(SwapSerializer, self).__init__(*args, **kwargs)

        try:
            if self.context['request'].method == 'PUT':
                pass
        except:
            pass


class UserSerializer(serializers.ModelSerializer):
    device = UserDeviceSerializer(read_only=True, many=True)

    class Meta:
        fields = ['id', 'username', 'email', 'device']
        model = get_user_model()


class TypeofDeviceSerializer(serializers.ModelSerializer):
    deviceUser = serializers.SerializerMethodField()

    def get_deviceUser(self, obj):
        if obj.deviceUser:
            return obj.deviceUser.username

    class Meta:
        fields = ['deviceName', 'deviceUser']
        model = Device


class Type_Retrieve_Serializer(serializers.ModelSerializer):
    devices = TypeofDeviceSerializer(read_only=True, many=True)

    class Meta:
        fields = ['id', 'typeName', 'devices']
        model = Type


class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['id', 'typeName']
        model = Type


class HistoryDevice(serializers.ModelSerializer):
    class Meta:
        model = LogDevice
        fields = ['logTitle', 'logTime']


class DeviceHistorySerializer(serializers.ModelSerializer):
    history = HistoryDevice(read_only=True, many=True)

    class Meta:
        fields = ['id', 'deviceName', 'deviceUser', 'deviceType', 'history']
        model = Device

    def get_deviceUser(self, obj):
        if obj.deviceUser:
            return obj.deviceUser.username

    def get_deviceType(self, obj):
        return obj.deviceType.typeName

    # Override method to show Device's username in GET method only.
    def __init__(self, *args, **kwargs):
        super(DeviceHistorySerializer, self).__init__(*args, **kwargs)

        try:
            if self.context['request'].method == 'GET':
                self.fields['deviceUser'] = serializers.SerializerMethodField()
                self.fields['deviceType'] = serializers.SerializerMethodField()
        except:
            pass


class DeviceSerializer(serializers.ModelSerializer):
    deviceUser = serializers.SerializerMethodField()

    class Meta:
        fields = ['id', 'deviceName', 'deviceUser', 'deviceType']
        model = Device

    def get_deviceUser(self, obj):
        if obj.deviceUser:
            return obj.deviceUser.username

    def get_deviceType(self, obj):
        return obj.deviceType.typeName

    # Override method to show Device's username in GET method only.
    def __init__(self, *args, **kwargs):
        super(DeviceSerializer, self).__init__(*args, **kwargs)

        try:
            if self.context['request'].method == 'GET':
                # self.fields['deviceUser'] = serializers.SerializerMethodField()
                self.fields['deviceType'] = serializers.SerializerMethodField()
        except:
            pass


class DeviceLogSerializer(serializers.ModelSerializer):
    logDevice = serializers.SerializerMethodField()

    def get_logDevice(self, obj):
        return obj.logDevice.deviceName

    class Meta:
        fields = ['id', 'logTitle', 'logDevice', 'logTime']
        model = LogDevice


class UserLogSerializer(serializers.ModelSerializer):
    logUser = serializers.SerializerMethodField()

    def get_logUser(self, obj):
        return obj.logUser.username

    class Meta:
        fields = ['id', 'logTitle', 'logUser', 'logTime']
        model = LogUser
