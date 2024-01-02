from django import forms
from django.contrib import admin

from suppliers.models import Supplier, Contacts, Products


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('name', 'provisioner', 'debt', 'created_at',)
    list_display_links = ('name', 'provisioner')
    list_filter = ('contacts__city',)
    actions = ["admin_action"]

    def get_readonly_fields(self, request, obj=None):
        """Запрещаем изменение поля "Задолженность" в том случае,
        если пользователь не имеет прав администратора"""
        if obj and not request.user.is_superuser:
            return 'debt',
        return self.readonly_fields

    def admin_action(self, request, queryset):
        """Доступ для администратора обнулять задолженность
        у выбранных объектов"""
        if request.user.is_superuser:
            queryset.update(debt=0)
        return None


@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    list_display = ('email', 'country',)


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ('name', 'model', 'release_date',)
