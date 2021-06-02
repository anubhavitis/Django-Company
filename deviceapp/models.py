from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth import get_user_model
from django.utils.timezone import now
from datetime import datetime
# Create your models here.


class Type(models.Model):
    typeName = models.CharField(max_length=50)

    def __str__(self):
        return self.typeName


class Device(models.Model):
    deviceName = models.CharField(max_length=100)
    deviceType = models.ForeignKey(Type, on_delete=CASCADE, related_name='devices')
    deviceUser = models.ForeignKey(
        get_user_model(), on_delete=CASCADE, blank=True, null=True, related_name="device")

    def __str__(self):
        return self.deviceName


class LogDevice(models.Model):
    logTitle = models.CharField(max_length=100)
    logDevice = models.ForeignKey(Device, on_delete=CASCADE, related_name='history')
    logTime =models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.logTitle


class LogUser(models.Model):
    logTitle = models.CharField(max_length=100)
    logUser = models.ForeignKey(get_user_model(), on_delete=CASCADE, related_name='history')
    logTime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.logTitle
