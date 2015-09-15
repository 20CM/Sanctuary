# -*- coding: utf-8 -*-

from rest_framework import serializers

from account.serializers import UserSerializer
from .models import Topic, Reply


class TopicSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)

    class Meta:
        model = Topic
        read_only_fields = (
            'created', 'modified', 'last_activity',
            'author', 'replies_count', 'id'
        )


class ReplySerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)

    class Meta:
        model = Reply
        read_only_fields = ('created', 'modified', 'author', 'index', 'content_html', 'id')
