from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser, models.Model):

    class Meta:
        verbose_name = "�û�"
        verbose_name_plural = "�û�"
