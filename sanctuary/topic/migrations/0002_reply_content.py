# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('topic', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reply',
            name='content',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
