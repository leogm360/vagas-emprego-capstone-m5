from rest_framework import permissions

from companies.models import Company


class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_superuser


class IsCompanyRecruiterOrAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        return request.user.is_superuser or request.user.is_human_resources

    def has_object_permission(self, request, view, obj: Company):

        if not request.user.is_authenticated:
            return False
        elif request.user.is_superuser:
            return True
        elif obj.id == request.user.company.id:
            return True
