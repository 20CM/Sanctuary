from rest_framework import viewsets
from rest_framework.permissions import SAFE_METHODS, IsAuthenticatedOrReadOnly, BasePermission

from .models import Tag
from .serializers import TagSerializer


class IsAdminUserOrModerator(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return  request.user and request.user.is_staff

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return request.user and (request.user.is_staff or request.user in obj.moderators)


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes=[IsAdminUserOrModerator]
