from django.contrib.auth import login, logout
from rest_framework import generics, viewsets
from rest_framework.filters import SearchFilter
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import authenticate
from suppliers.models import Supplier, Contacts, Products
from suppliers.serializers import SuppliersListSerializer, SupplierSerializer, ContactsSerializer, ProductsSerializer, \
    SupplierUpdateSerializer


class SupplierCreateApiView(generics.CreateAPIView):
    serializer_class = SupplierSerializer


class SupplierRetrieveApiView(generics.RetrieveAPIView):
    serializer_class = SuppliersListSerializer
    queryset = Supplier.objects.all()


class SupplierUpdateApiView(generics.UpdateAPIView):
    serializer_class = SupplierUpdateSerializer
    queryset = Supplier.objects.all()


class SupplierDeleteApiView(generics.DestroyAPIView):
    serializer_class = SupplierSerializer
    queryset = Supplier.objects.all()


class SupplierListApiView(generics.ListAPIView):
    serializer_class = SuppliersListSerializer
    queryset = Supplier.objects.all()
    filter_backends = [SearchFilter]
    search_fields = ['contacts__country']


class ContactsViewSet(viewsets.ModelViewSet):
    serializer_class = ContactsSerializer
    queryset = Contacts.objects.all()


class ProductsViewSet(viewsets.ModelViewSet):
    serializer_class = ProductsSerializer
    queryset = Products.objects.all()
