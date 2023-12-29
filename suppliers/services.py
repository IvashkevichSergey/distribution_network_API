from django.contrib.auth import authenticate, login, logout, get_user_model
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics

from suppliers.serializers import UserSerializer, UserEditSerializer


class UserView(generics.CreateAPIView):
    model = get_user_model()
    permission_classes = [AllowAny]
    serializer_class = UserSerializer


class UserRetrieveView(generics.RetrieveUpdateDestroyAPIView):
    queryset = get_user_model().objects
    permission_classes = [IsAuthenticated]
    serializer_class = UserEditSerializer

    def get_object(self):
        return self.request.user

class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(
            request=request,
            username=username,
            password=password,
        )
        if not user:
            return Response("Похоже что Ваша учётная запись не активна, обратитесь к администратору")

        login(request, user)
        return Response("Вы успешно вошли в систему")


class LogoutView(APIView):
    def post(self, request):
        logout(request)
        return Response("Вы успешно вышли из системы")
