from rest_framework import generics

from suppliers.models import Supplier
from suppliers.serializers import SuppliersListSerializer, SupplierSerializer


class SupplierCreateApiView(generics.CreateAPIView):
    serializer_class = SupplierSerializer


class SupplierRetrieveApiView(generics.RetrieveAPIView):
    serializer_class = SuppliersListSerializer
    queryset = Supplier.objects.all()


class SupplierUpdateApiView(generics.UpdateAPIView):
    serializer_class = SupplierSerializer
    queryset = Supplier.objects.all()


class SupplierDeleteApiView(generics.DestroyAPIView):
    serializer_class = SupplierSerializer
    queryset = Supplier.objects.all()


class SupplierListApiView(generics.ListAPIView):
    serializer_class = SuppliersListSerializer
    queryset = Supplier.objects.all()
