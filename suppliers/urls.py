from django.urls import path
from rest_framework.routers import DefaultRouter
from suppliers.apps import SuppliersConfig
from suppliers.views import SupplierCreateApiView, SupplierDeleteApiView, \
    SupplierRetrieveApiView, SupplierUpdateApiView, SupplierListApiView, \
    ContactsViewSet, ProductsViewSet

app_name = SuppliersConfig.name

router = DefaultRouter()
router.register(r'contacts', ContactsViewSet)
router.register(r'products', ProductsViewSet)

urlpatterns = [
    path('create/', SupplierCreateApiView.as_view()),
    path('<int:pk>/', SupplierRetrieveApiView.as_view()),
    path('<int:pk>/delete', SupplierDeleteApiView.as_view()),
    path('<int:pk>/update', SupplierUpdateApiView.as_view()),
    path('', SupplierListApiView.as_view()),
] + router.urls
