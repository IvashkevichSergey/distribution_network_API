from rest_framework.permissions import BasePermission


class IsActivePermission(BasePermission):
    """Класс для проверки доступа к сети только для активных пользователей"""
    def has_permission(self, request, view):
        return request.user.is_active

