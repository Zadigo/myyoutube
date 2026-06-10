from rest_framework.permissions import BasePermission


class CanComment(BasePermission):
    def has_permission(self, request, view):
        return all([
            request.user is not None,
            request.user.is_staff
        ])
