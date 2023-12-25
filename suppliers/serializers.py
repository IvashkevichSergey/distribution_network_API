from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from suppliers.models import Supplier, Contacts, Products


class ContactsSerializer(ModelSerializer):
    class Meta:
        model = Contacts
        exclude = 'id',


class ProductsSerializer(ModelSerializer):
    class Meta:
        model = Products
        exclude = 'id',


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
