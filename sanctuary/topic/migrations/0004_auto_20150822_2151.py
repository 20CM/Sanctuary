# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('topic', '0003_auto_20150822_2040'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='last_update',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='topic',
            name='replies_count',
            field=models.IntegerField(default=0),
        ),
    ]
