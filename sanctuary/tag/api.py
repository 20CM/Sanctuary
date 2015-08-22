from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser

from .models import Tag
from .serializers import TagSerializer


class IsAdminUserOrModerator(IsAdminUser):
    def has_object_permission(self, request, view, obj):
        return self.has_permission(request, view) or request.user in obj.moderators


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes=[IsAdminUserOrModerator]
