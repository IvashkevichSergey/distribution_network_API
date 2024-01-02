from django.contrib.auth.models import Group, Permission
from django.core.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from suppliers.models import Supplier, Contacts, Products
from django.contrib.auth import get_user_model


class ContactsSerializer(ModelSerializer):
    """Сериализатор для модели Контактов"""
    class Meta:
        model = Contacts
        fields = '__all__'


class ProductsSerializer(ModelSerializer):
    """Сериализатор для модели Продукции"""
    class Meta:
        model = Products
        fields = '__all__'


class SuppliersListSerializer(ModelSerializer):
    """Сериализатор для списка всех поставщиков"""
    contacts = ContactsSerializer(many=True)
    products = ProductsSerializer(many=True)
    provisioner = serializers.SerializerMethodField(source='provisioner')

    def get_provisioner(self, obj):
        if obj.provisioner:
            return obj.provisioner.name
        return '-'

    class Meta:
        model = Supplier
        fields = '__all__'


class SupplierSerializer(ModelSerializer):
    """Сериализатор для создания и удаления объекта поставщика"""
    def save(self, **kwargs):
        return super(SupplierSerializer, self).save(**kwargs)

    class Meta:
        model = Supplier
        fields = '__all__'


class SupplierUpdateSerializer(ModelSerializer):
    """Сериализатор для изменения объекта поставщика с
    запретом на изменение задолженности"""
    debt = serializers.DecimalField(
        max_digits=12, decimal_places=2, read_only=True
    )

    class Meta:
        model = Supplier
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    """Сериализатор для создания нового пользователя"""
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = get_user_model().objects.create_user(**validated_data)

        # Каждый пользователь при регистрации получает статус "Персонал"
        user.is_staff = True

        # Каждый пользователь при регистрации добавляется в группу
        # Staff с необходимыми разрешениями для работы с сервисом
        group, created = Group.objects.get_or_create(name='Staff')
        if created:
            permissions_list = Permission.objects.filter(
                content_type__app_label='suppliers'
            )
            group.permissions.set(permissions_list)

        user.groups.add(group)
        user.save()
        return user

    class Meta:
        model = get_user_model()
        fields = ("id", "username", "password",)


class UserEditSerializer(serializers.ModelSerializer):
    """Сериализатор для редактирования пользователя"""
    password = serializers.CharField(write_only=True)

    class Meta:
        model = get_user_model()
        fields = ("username", "password", "first_name", "last_name", "email")
