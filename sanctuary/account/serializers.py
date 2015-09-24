# -*- coding: utf-8 -*-

from rest_framework import serializers

from .models import CustomUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'email', 'username', 'is_active', 'date_joined', "password", "is_staff")
        read_only_fields = ('id', 'is_active', 'date_joined', 'is_staff')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        if not CustomUser.objects.count():
            # The first user will be a superuser
            user.is_superuser = True
            user.is_staff = True
        user.save()
        return user


class SimplifiedUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'email', 'username')


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('email', 'username', 'password')


class PasswordSerializer(serializers.Serializer):
    password = serializers.CharField(max_length=200)
