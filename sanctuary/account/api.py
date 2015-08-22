from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import detail_route, list_route
from rest_framework.response import Response
from rest_framework.permissions import BasePermission, SAFE_METHODS
from rest_framework.mixins import UpdateModelMixin

from .models import CustomUser
from .serializers import UserSerializer, PasswordSerializer, RegisterSerializer


class IsSuperAdminOrSelfPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        user = request.user

        return user.is_superuser or user == obj


class UserViewSet(UpdateModelMixin, viewsets.ReadOnlyModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes=[IsSuperAdminOrSelfPermission]

    @detail_route(methods=['post'], url_path='change-password')
    def set_password(self, request, pk=None):
        user = self.get_object()
        serializer = PasswordSerializer(data=request.data)
        if serializer.is_valid():
            user.set_password(serializer.data['password'])
            user.save()
            return Response({'status': 'password set'})
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    @list_route(methods=["post"])
    def register(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = CustomUser.objects.create_user(
                username=serializer.data["username"],
                password=serializer.data["password"],
                email=serializer.data["email"]
            )
            return Response({'status': 'user created'})
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)
