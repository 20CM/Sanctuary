from django.db import models
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver

from django_extensions.db.fields import (
    AutoSlugField,
    CreationDateTimeField,
    ModificationDateTimeField
)

from account.models import CustomUser
from tag.models import Tag


class Topic(models.Model):
    title = models.CharField(max_length=50)
    slug = AutoSlugField(populate_from="title")
    content = models.TextField(blank=True)
    created = CreationDateTimeField()
    updated = ModificationDateTimeField()
    last_update = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(CustomUser, related_name="topics")
    tags = models.ManyToManyField(Tag, related_name="topics", blank=True)

    replies_count = models.IntegerField(default=0)


@receiver(post_save, sender=Topic)
def update_tag_info(sender, instance, created, **kwargs):
    if created:
        return
    for tag in instance.tags:
        tag.topics_count += 1
        tag.save()


class Reply(models.Model):
    topic = models.ForeignKey(Topic, related_name="replies")
    author = models.ForeignKey(CustomUser, related_name="replies")
    content = models.TextField()
    created = CreationDateTimeField()
    updated = ModificationDateTimeField()


@receiver(post_save, sender=Reply)
def update_topic_info(sender, instance, created, **kwargs):
    if created:
        return
    instance.topic.replies_count += 1
    instance.topic.last_update = instance.created
    instance.topic.save()
