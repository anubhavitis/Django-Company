from django.contrib import admin
from .models import LogDevice, LogUser, Device, Type

# Register your models here.

admin.site.register(LogUser)
admin.site.register(LogDevice)
admin.site.register(Device)
admin.site.register(Type)
