from rest_framework.permissions import BasePermission, SAFE_METHODS

from accounts.models import Responder


class IsOwnerOrReadOnly(BasePermission):
    message = 'permission denied, you are not the owner'

    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.author == request.user


class IsOwner(BasePermission):
    message = 'permission denied, you are not the owner'

    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj == request.user


