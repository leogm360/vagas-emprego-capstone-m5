from rest_framework import permissions


class CompaniesCustomPermissions(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method in  permissions.SAFE_METHODS:
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
