from rest_framework import permissions

from companies.models import Company


class CompaniesCustomPermissions(permissions.BasePermission):

    # def has_object_permission(self, request, view, obj):
    #     if request.method in "PATCH":
    #      return (request.user.is_authenticated and obj == request.user.company_id or request.user.is_authenticated and request.user.is_superuser )

    def has_permission(self, request, view):
        if request.method in "GET":
            return True
        if request.method in "POST" and request.user.is_superuser:
            return True

        return request.user.is_superuser


class IsRecruiterOrAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False

        return request.user.is_superuser

    # Esperando incluir company_id no usuário Recruiter, para poder terminar permission

    # def has_object_permission(self, request, view, obj: Company):
    #     return obj.id == request.user
