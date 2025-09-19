from rest_framework.permissions import (
    AllowAny,
    BasePermission,
    IsAuthenticated,
    IsAuthenticatedOrReadOnly,
)

__all__ = [
    "AllowAny",
    "IsAuthenticated",
    "IsAuthenticatedOrReadOnly",
    "IsOwner",
    "BasePermission",
]


class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user == obj.owner
