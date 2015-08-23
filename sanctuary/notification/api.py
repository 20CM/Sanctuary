from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.permissions import BasePermission

from .models import Notification
from .serializers import NotificationSerializer


class IsReceiver(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user and request.user == obj.receiver


class NotificationViewSet(ReadOnlyModelViewSet):
    queryset = Notification.objects.receiver(None)
    serializer_class = NotificationSerializer
    permission_classes=[IsReceiver]
    filter_fields = ('topic', 'is_read')

    def get_queryset(self):
        user = self.request.user
        return Notification.objects.receiver(user)
