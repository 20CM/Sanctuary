# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('topic', '0007_auto_20150823_1848'),
    ]

    operations = [
        migrations.AddField(
            model_name='reply',
            name='content_html',
            field=models.TextField(blank=True),
        ),
        migrations.AlterUniqueTogether(
            name='reply',
            unique_together=set([('topic', 'index')]),
        ),
        migrations.AlterUniqueTogether(
            name='topic',
            unique_together=set([]),
        ),
    ]
