# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import model_utils.fields
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('topic', '0005_auto_20150823_1705'),
    ]

    operations = [
        migrations.RenameField(
            model_name='topic',
            old_name='last_update',
            new_name='last_activity',
        ),
        migrations.RemoveField(
            model_name='reply',
            name='updated',
        ),
        migrations.RemoveField(
            model_name='topic',
            name='updated',
        ),
        migrations.AddField(
            model_name='reply',
            name='modified',
            field=model_utils.fields.AutoLastModifiedField(verbose_name='modified', editable=False, default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='topic',
            name='modified',
            field=model_utils.fields.AutoLastModifiedField(verbose_name='modified', editable=False, default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='reply',
            name='created',
            field=model_utils.fields.AutoCreatedField(verbose_name='created', editable=False, default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='topic',
            name='created',
            field=model_utils.fields.AutoCreatedField(verbose_name='created', editable=False, default=django.utils.timezone.now),
        ),
    ]
