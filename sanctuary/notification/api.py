from rest_framework import status
from rest_framework.decorators import detail_route, list_route
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.permissions import BasePermission

from .models import Notification
from .serializers import (
    NotificationSerializer, MarkNotificationAsReadConfirmSerializer,
    MarkNotificationsOfTopicSerializer
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
        """
        ---
        serializer: MarkNotificationAsReadConfirmSerializer
        """
        notification = self.get_object()
        serializer = MarkNotificationAsReadConfirmSerializer(data=request.data)
        if serializer.is_valid() and serializer.data['username'] == request.user.username:
            notification.is_read = True
            notification.save()
            return Response({'status': 'marked'})
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    @list_route(methods=["post"])
    def mark_as_read(self, request):
        """
        ---
        serializer: MarkNotificationsOfTopicSerializer
        """

        serializer = MarkNotificationsOfTopicSerializer(data=request.data)
        if serializer.is_valid():
            notifications = self.get_queryset().filter(topic=serializer.data['topic']).unread()
            count = notifications.count()
            notifications.update(is_read=True)
            return Response({'status': 'marked {} notifications'.format(count)})
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)
