# -*- coding: utf-8 -*-

from rest_framework import serializers

from account.serializers import SimplifiedUserSerializer
from .models import Topic, Reply


class TopicSerializer(serializers.ModelSerializer):
    author = SimplifiedUserSerializer(read_only=True)

    class Meta:
        model = Topic
        read_only_fields = (
            'created', 'modified', 'last_activity',
            'author', 'replies_count', 'id'
        )


class ReplySerializer(serializers.ModelSerializer):
    author = SimplifiedUserSerializer(read_only=True)

    class Meta:
        model = Reply
        read_only_fields = ('created', 'modified', 'author', 'index', 'content_html', 'id')
