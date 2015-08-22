from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser, models.Model):

    class Meta:
        verbose_name = "用户"
        verbose_name_plural = "用户"
