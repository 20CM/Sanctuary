# -*- coding: utf-8 -*-

from django.db import models


class NotificationQuerySet(models.QuerySet):
    def receiver(self, user):
        return self.filter(receiver=user)

    def unread(self):
        return self.filter(is_read=False)

    def read_all(self, user):
        return self.receiver(user).update(is_read=True)
