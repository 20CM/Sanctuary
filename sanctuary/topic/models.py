from django.db import models

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
    author = models.ForeignKey(CustomUser, related_name="topics")
    tags = models.ManyToManyField(Tag, related_name="topics")


class Reply(models.Model):
    topic = models.ForeignKey(Topic, related_name="replies")
    author = models.ForeignKey(CustomUser, related_name="replies")
    created = CreationDateTimeField()
    updated = ModificationDateTimeField()
