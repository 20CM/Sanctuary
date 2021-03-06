from django.db import models

from model_utils.models import TimeStampedModel

from account.models import CustomUser
from topic.models import Topic, Reply

from .managers import NotificationQuerySet


class Notification(TimeStampedModel):
    sender = models.ForeignKey(CustomUser, blank=True)
    topic = models.ForeignKey(Topic)
    reply = models.ForeignKey(Reply)
    receiver = models.ForeignKey(CustomUser, related_name="notifications", db_index=True)

    is_read = models.BooleanField(default=False)

    objects = NotificationQuerySet.as_manager()

    class Meta:
        unique_together = ("receiver", "reply")

    @classmethod
    def create_notifications_from_reply(cls, reply, mentions):
        for user in mentions.values():
            cls.objects.get_or_create(
                sender=reply.author,
                topic=reply.topic,
                reply=reply,
                receiver=user
            )
