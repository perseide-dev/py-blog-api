from rest_framework import permissions

class IsAuthorOrReadOnly(permissions.BasePermission): 
    # Custom permission to only allow authors of a post to edit or delete it.
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        if request.user and request.user.is_staff:
            return True
        return getattr(obj, 'author', None) == request.user