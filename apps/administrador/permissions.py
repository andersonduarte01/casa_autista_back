from rest_framework import permissions

class IsAdministrador(permissions.BasePermission):

    def has_permission(self, request, view):
        return bool(
            request.user
            and request.user.is_authenticated
            and getattr(request.user, "is_administrator", False)
        )
