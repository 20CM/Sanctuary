from django.db import models
from django.db.models import F
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.utils import timezone

from model_utils.models import TimeStampedModel
from django_extensions.db.fields import AutoSlugField

from account.models import CustomUser
from tag.models import Tag
from .markdown.markdown import Markdown


class Topic(TimeStampedModel):
    title = models.CharField(max_length=50)
    slug = AutoSlugField(populate_from="title")
    last_activity = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(CustomUser, related_name="topics")
    tags = models.ManyToManyField(Tag, related_name="topics", blank=True)

    replies_count = models.IntegerField(default=0)


class Reply(TimeStampedModel):
    topic = models.ForeignKey(Topic, related_name="replies")
    index = models.IntegerField(default=0)
    author = models.ForeignKey(CustomUser, related_name="replies")
    content = models.TextField()
    content_html = models.TextField(blank=True)

    class Meta:
        unique_together = ("topic", "index")

    def save(self, *args, **kwargs):
        markdown = Markdown()
        self.content_html = markdown.render(self.content)
        super().save(*args, **kwargs)
        from notification.models import Notification
        Notification.create_notifications_from_reply(
            reply=self,
            mentions=markdown.get_mentions()
        )


@receiver(pre_save, sender=Reply)
def calc_index(sender, instance, **kwargs):
    if instance.index == 0:
        instance.index = instance.topic.replies_count + 1


@receiver(post_save, sender=Reply)
def update_topic_replies_count(sender, instance, created, **kwargs):
    if not created:
        return
    topic = instance.topic
    topic.replies_count = F("replies_count") + 1
    topic.last_activity = instance.created
    topic.save()
