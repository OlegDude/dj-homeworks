from rest_framework import permissions


class IsAdminOwnerOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):

        if request.method in permissions.SAFE_METHODS:
            return True
        elif request.user and request.user.is_staff:
            return True

        return obj.creator.id == request.user.id


class IsOwnerReadDraft(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            if obj.status == 'DRAFT':
                return obj.creator.id == request.user.id or request.user.is_staff

            return True

