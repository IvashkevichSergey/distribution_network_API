from django.contrib.auth.models import Group
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from suppliers.models import Supplier, Contacts, Products
from django.contrib.auth import get_user_model


class ContactsSerializer(ModelSerializer):
    class Meta:
        model = Contacts
        fields = '__all__'


class ProductsSerializer(ModelSerializer):
    class Meta:
        model = Products
        fields = '__all__'


class SuppliersListSerializer(ModelSerializer):
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
    class Meta:
        model = Supplier
        fields = '__all__'


class SupplierUpdateSerializer(ModelSerializer):
    debt = serializers.DecimalField(max_digits=12, decimal_places=2, read_only=True)

    class Meta:
        model = Supplier
        fields = '__all__'


UserModel = get_user_model()
group = Group.objects.get(name='Staff')


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = UserModel.objects.create_user(**validated_data)
        user.is_staff = True
        user.groups.add(group)
        user.save()
        return user

    class Meta:
        model = UserModel
        fields = ("id", "username", "password",)


class UserEditSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = UserModel
        fields = ("username", "password", "first_name", "last_name", "email")
