# -*- coding: utf-8 -*-

from rest_framework import serializers

from .models import Notification


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification


class MarkNotificationsAsReadSerializer(serializers.Serializer):
    topic = serializers.IntegerField(required=False, allow_null=True)
