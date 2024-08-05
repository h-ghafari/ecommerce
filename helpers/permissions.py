from rest_framework.permissions import BasePermission

class IsRelatedOrAdmin(BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.user.is_staff:
            return True
        if obj.user == request.user:
            return True
        return False
    
class IsSelfOrAdmin(BasePermission):
    
    def has_object_permission(self, request, view, obj):
        if request.user.is_staff:
            return True
        if request.user == obj:
            return True
        return False
    
