from django.db import models

from django_extensions.db.fields import AutoSlugField

from account.models import CustomUser


class Tag(models.Model):
    name = models.CharField(max_length=20, unique=True, db_index=True)
    slug = AutoSlugField(populate_from="name")
    description = models.TextField(blank=True, default="")
    moderators = models.ManyToManyField(CustomUser, blank=True)
