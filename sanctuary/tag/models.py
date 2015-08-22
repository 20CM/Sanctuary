from django.db import models

from django_extensions.db.fields import AutoSlugField

from account.models import CustomUser


class Tag(models.Model):
    name = models.CharField(max_length=20)
    slug = AutoSlugField(populate_from="name")
    moderators = models.ManyToManyField(CustomUser)
