from rest_framework import permissions

class CompaniesCustomPermissions(permissions.BasePermission):

    # def has_object_permission(self, request, view, obj):
    #     if request.method in "PATCH":
    #      return (request.user.is_authenticated and obj == request.user.company_id or request.user.is_authenticated and request.user.is_superuser )

    def has_permission(self, request, view):
        if request.method in "GET":
                return  True

        return (request.user.is_authenticated and request.user.is_human_resources or request.user.is_authenticated and request.user.is_superuser )