from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser, models.Model):
    def get_absolute_url(self):
        return "/user/{}".format(self.username)
