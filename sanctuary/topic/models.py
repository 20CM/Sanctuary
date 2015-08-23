from django.db import models
from django.utils import timezone

from model_utils.models import TimeStampedModel
from django_extensions.db.fields import AutoSlugField

from account.models import CustomUser
from tag.models import Tag


class Topic(TimeStampedModel):
    title = models.CharField(max_length=50)
    slug = AutoSlugField(populate_from="title")
    last_activity = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(CustomUser, related_name="topics")
    tags = models.ManyToManyField(Tag, related_name="topics", blank=True)

    replies_count = models.IntegerField(default=0)

    class Meta:
        unique_together = ("title", "author")


class Reply(TimeStampedModel):
    topic = models.ForeignKey(Topic, related_name="replies")
    index = models.IntegerField(default=0)
    author = models.ForeignKey(CustomUser, related_name="replies")
    content = models.TextField()

    class Meta:
        unique_together = (("topic", "index"), ("topic", "content", "author"))

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if not self.index:
            topic = self.topic
            topic.replies_count += 1
            topic.last_activity = self.created
            topic.save()
            self.index = self.topic.replies_count
        return super().save(force_insert, force_update, using, update_fields)
