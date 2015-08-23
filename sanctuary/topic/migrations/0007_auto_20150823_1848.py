# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('topic', '0006_auto_20150823_1739'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='reply',
            unique_together=set([('topic', 'index'), ('topic', 'content', 'author')]),
        ),
        migrations.AlterUniqueTogether(
            name='topic',
            unique_together=set([('title', 'author')]),
        ),
    ]
