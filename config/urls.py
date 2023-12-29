from django.contrib import admin
from django.urls import path, include
from suppliers.services import LoginView, LogoutView, UserView, UserRetrieveView

urlpatterns = [
    path('admin/', admin.site.urls),

    path('register/', UserView.as_view()),
    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('profile/', UserRetrieveView.as_view()),

    path('supplier/', include('suppliers.urls'))
]
