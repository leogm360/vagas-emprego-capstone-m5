from rest_framework import permissions

from .models import Account

class IsOwnerAccountOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj: Account):
        return obj == request.user


class IsCandidateOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj: Account):
        return (
            obj.is_human_resources == False
            and
            obj.is_human_resources == request.user.is_human_resources
            and
            obj == request.user
        )

class IsRecruiterOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj: Account):
        return (
            obj.is_human_resources == True
            and
            obj.is_human_resources == request.user.is_human_resources
            and
            obj == request.user
        )  

class IsAdmOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_superuser