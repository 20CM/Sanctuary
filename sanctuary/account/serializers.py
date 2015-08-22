# -*- coding: utf-8 -*-

from rest_framework import serializers

from .models import CustomUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'email', 'username', 'is_active', 'date_joined')


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('email', 'username', 'password')


class PasswordSerializer(serializers.Serializer):
    password = serializers.CharField(max_length=200)
