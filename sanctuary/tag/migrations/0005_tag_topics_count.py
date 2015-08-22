# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tag', '0004_auto_20150822_2135'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='topics_count',
            field=models.IntegerField(default=0),
        ),
    ]
