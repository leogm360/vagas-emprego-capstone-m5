from rest_framework import permissions
from rest_framework.views import Request

from .models import Account


class IsOwnerAccountOnly(permissions.BasePermission):
    def has_object_permission(self, request: Request, view, obj: Account):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.account_id == request.user.id


class IsOwnerOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view, obj: Account):
        if request.method in permissions.SAFE_METHODS:
            if request.user.is_superuser:
                return True
            return obj == request.user

        return obj == request.user


class IsCandidateOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        return (
            request.user.is_authenticated and request.user.is_human_resources == False
        )


class IsRecruiterOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        return (
            request.user.is_authenticated
        and request.user.is_human_resources == True
        )


class IsAdmOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_superuser
