from rest_framework import permissions

class IsAuthenticatedOrReadOnly(permissions.BasePermission):
    """
    Custom permission: 
    - SAFE_METHODS (GET, HEAD, OPTIONS) are allowed for anyone.
    - Other methods require authentication.
    """

    def has_permission(self, request, view):
        # Allow GET, HEAD, OPTIONS for all
        if request.method in permissions.SAFE_METHODS:
            return True
        # For POST, PUT, PATCH, DELETE → must be logged in
        return request.user and request.user.is_authenticated
