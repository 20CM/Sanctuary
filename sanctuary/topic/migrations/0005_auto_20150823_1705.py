# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import topic.models


class Migration(migrations.Migration):

    dependencies = [
        ('topic', '0004_auto_20150822_2151'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='topic',
            name='content',
        ),
        migrations.AddField(
            model_name='reply',
            name='index',
            field=models.IntegerField(default=0),
        ),
    ]
