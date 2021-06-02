from rest_framework import permissions

class LogRetrivePermissions(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.method in ['GET']
class LogPermissions(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.method in ['GET']