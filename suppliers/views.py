from rest_framework import generics, viewsets
from rest_framework.filters import SearchFilter
from suppliers.models import Supplier, Contacts, Products
from suppliers.serializers import SuppliersListSerializer, SupplierSerializer, ContactsSerializer, ProductsSerializer, \
    SupplierUpdateSerializer


class SupplierCreateApiView(generics.CreateAPIView):
    """Контроллер для создания нового объекта сервиса"""
    serializer_class = SupplierSerializer
    queryset = Supplier.objects.all()


class SupplierRetrieveApiView(generics.RetrieveAPIView):
    """Контроллер для просмотра информации об объекте"""
    serializer_class = SuppliersListSerializer
    queryset = Supplier.objects.all()


class SupplierUpdateApiView(generics.UpdateAPIView):
    """Контроллер для изменения данных об объекте"""
    serializer_class = SupplierUpdateSerializer
    queryset = Supplier.objects.all()


class SupplierDeleteApiView(generics.DestroyAPIView):
    """Контроллер для удаления объекта"""
    serializer_class = SupplierSerializer
    queryset = Supplier.objects.all()


class SupplierListApiView(generics.ListAPIView):
    """Контроллер для просмотра списка объектов"""
    serializer_class = SuppliersListSerializer
    queryset = Supplier.objects.all()
    filter_backends = [SearchFilter]
    search_fields = ['contacts__country']


class ContactsViewSet(viewsets.ModelViewSet):
    """Контроллер для управления моделью контактов"""
    serializer_class = ContactsSerializer
    queryset = Contacts.objects.all()


class ProductsViewSet(viewsets.ModelViewSet):
    """Контроллер для управления моделью продуктов"""
    serializer_class = ProductsSerializer
    queryset = Products.objects.all()
