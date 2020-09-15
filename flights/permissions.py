from rest_framework import permissions

class is_THEauthenticated(permissions.BasePermission):
    message = 'You don\'t have any bookings'

    def has_object_permission(self, request, view, obj):
        if request.user == obj.user:
            return True
        else:
            return False


class CanUpdate(permissions.BasePermission):
    message = 'You don\'t have access'

    def has_object_permission(self, request, view, obj):
        if request.user == obj.user:
            return True
        else:
            return False
