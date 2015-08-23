from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import BasePermission, SAFE_METHODS, IsAuthenticatedOrReadOnly

from .models import Topic, Reply
from sanctuary.viewsets import NoDestroyModelViewSet
from .serializers import TopicSerializer, ReplySerializer


class CreateWithAuthorMixin(object):
    """
    Create a model instance.
    """
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class IsSuperAdminOrAuthor(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        user = request.user

        return user.is_superuser or user == obj.author


class TopicViewSet(CreateWithAuthorMixin, NoDestroyModelViewSet):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, IsSuperAdminOrAuthor)
    filter_fields = ('author', 'tags')


class ReplyViewSet(CreateWithAuthorMixin, NoDestroyModelViewSet):
    queryset = Reply.objects.all()
    serializer_class = ReplySerializer
    permission_classes = (IsAuthenticatedOrReadOnly, IsSuperAdminOrAuthor)
    filter_fields = ('topic', 'author')
