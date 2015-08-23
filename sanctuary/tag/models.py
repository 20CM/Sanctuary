from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from django_extensions.db.fields import AutoSlugField

from account.models import CustomUser


class Tag(models.Model):
    name = models.CharField(max_length=20, unique=True, db_index=True)
    slug = AutoSlugField(populate_from="name")
    description = models.TextField(blank=True, default="")
    moderators = models.ManyToManyField(CustomUser, blank=True)

    topics_count = models.IntegerField(default=0)


@receiver(post_save, sender="topic.Topic")
def update_tag_info(sender, instance, created, **kwargs):
    if not created:
        return True
    for tag in instance.tags.all():
        tag.topics_count += 1
        tag.save()
    return True
