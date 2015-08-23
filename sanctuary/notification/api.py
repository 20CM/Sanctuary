from rest_framework import status
from rest_framework.decorators import detail_route, list_route
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.permissions import BasePermission

from .models import Notification
from .serializers import (
    NotificationSerializer, MarkNotificationsAsReadSerializer
)


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

    @detail_route(methods=['post'])
    def read(self, request, pk=None):
        notification = self.get_object()
        notification.is_read = True
        notification.save()
        return Response({'status': 'marked'})

    @list_route(methods=["post"])
    def mark_as_read(self, request):
        """
        ---
        serializer: MarkNotificationsAsReadSerializer
        """

        serializer = MarkNotificationsAsReadSerializer(data=request.data)
        if serializer.is_valid():
            if serializer.data["topic"]:
                notifications = self.get_queryset().filter(topic_id=serializer.data["topic"])
            else:
                notifications = self.get_queryset().all()
            notifications = notifications.unread()
            count = notifications.count()
            notifications.update(is_read=True)
            return Response({'status': 'marked {} notifications'.format(count)})
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)
