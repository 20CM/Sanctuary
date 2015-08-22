# -*- coding: utf-8 -*-

from rest_framework import serializers

from .models import Tag


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        read_only_fields = ('topics_count',)