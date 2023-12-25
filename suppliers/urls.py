from django.urls import path

from suppliers.apps import SuppliersConfig
from suppliers.views import SupplierCreateApiView, SupplierDeleteApiView, \
    SupplierRetrieveApiView, SupplierUpdateApiView, SupplierListApiView

app_name = SuppliersConfig.name

urlpatterns = [
    path('create/', SupplierCreateApiView.as_view()),
    path('<int:pk>/', SupplierRetrieveApiView.as_view()),
    path('<int:pk>/delete', SupplierDeleteApiView.as_view()),
    path('<int:pk>/update', SupplierUpdateApiView.as_view()),
    path('', SupplierListApiView.as_view()),
]
