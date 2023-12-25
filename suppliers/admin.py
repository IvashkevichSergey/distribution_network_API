from django.contrib import admin
from django.utils.html import format_html

from suppliers.models import Supplier, Contacts, Products


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('name', 'provisioner', 'debt', 'created_at',)
    list_display_links = ('name', 'provisioner')
    list_filter = ('contacts__city',)
    actions = ["admin_action"]

    def get_readonly_fields(self, request, obj=None):
        if obj and not request.user.is_superuser:
            return 'debt',
        return self.readonly_fields

    def admin_action(self, request, queryset):
        queryset.update(debt=0)


@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    list_display = ('email', 'country',)


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ('name', 'model', 'release_date',)
