# -*- coding: utf-8 -*-

from rest_framework import serializers

from .models import Notification


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification


class MarkNotificationAsReadConfirmSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=200)


class MarkNotificationsOfTopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ('topic', )
