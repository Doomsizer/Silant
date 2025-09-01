from rest_framework.permissions import BasePermission

class IsClient(BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name='Client').exists()

class IsServiceOrganization(BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name='ServiceOrganization').exists()

class IsManager(BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name='Manager').exists()

class CanViewCar(BasePermission):
    def has_permission(self, request, view):
        return True

class CanEditCar(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and IsManager().has_permission(request, view)

class CanViewMaintenance(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and (
            IsClient().has_permission(request, view) or
            IsServiceOrganization().has_permission(request, view) or
            IsManager().has_permission(request, view)
        )

class CanEditMaintenance(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and (
            IsClient().has_permission(request, view) or
            IsServiceOrganization().has_permission(request, view) or
            IsManager().has_permission(request, view)
        )

class CanViewReclaim(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and (
            IsClient().has_permission(request, view) or
            IsServiceOrganization().has_permission(request, view) or
            IsManager().has_permission(request, view)
        )

class CanEditReclaim(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and (
            IsServiceOrganization().has_permission(request, view) or
            IsManager().has_permission(request, view)
        )