from rest_framework import status
from rest_framework.decorators import detail_route, list_route
from rest_framework.response import Response
from rest_framework.permissions import BasePermission, SAFE_METHODS
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.models import Token

from .models import CustomUser
from sanctuary.viewsets import NoDestroyModelViewSet
from .serializers import UserSerializer, PasswordSerializer


class IsSuperAdminOrSelfPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        user = request.user

        return user.is_superuser or user == obj


class UserViewSet(NoDestroyModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes=[IsSuperAdminOrSelfPermission]
    filter_fields = ('username',)

    @detail_route(methods=['post'], url_path='change-password')
    def set_password(self, request, pk=None):
        """
        ---
        serializer: PasswordSerializer
        """
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
    def obtain_auth_token(self, request):
        """
        ---
        serializer: AuthTokenSerializer
        """
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key,
                         'id': user.id})
