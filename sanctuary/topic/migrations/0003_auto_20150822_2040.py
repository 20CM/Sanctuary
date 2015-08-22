# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('topic', '0002_reply_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='tags',
            field=models.ManyToManyField(related_name='topics', blank=True, to='tag.Tag'),
        ),
    ]
