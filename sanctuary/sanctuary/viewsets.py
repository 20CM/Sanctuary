# -*- coding: utf-8 -*-
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet


class NoDestroyModelViewSet(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.ListModelMixin,
                   GenericViewSet):
    pass
