# -*- coding: utf-8 -*-

from rest_framework import serializers

from .models import Topic, Reply


class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        read_only_fields = (
            'created', 'modified', 'last_activity',
            'author', 'replies_count',
        )


class ReplySerializer(serializers.ModelSerializer):
    class Meta:
        model = Reply
        read_only_fields = ('created', 'modified', 'author', 'index')
