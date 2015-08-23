# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('topic', '0006_auto_20150823_1739'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('created', model_utils.fields.AutoCreatedField(editable=False, verbose_name='created', default=django.utils.timezone.now)),
                ('modified', model_utils.fields.AutoLastModifiedField(editable=False, verbose_name='modified', default=django.utils.timezone.now)),
                ('is_read', models.BooleanField(default=False)),
                ('receiver', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='notifications')),
                ('reply', models.ForeignKey(to='topic.Reply')),
                ('sender', models.ForeignKey(to=settings.AUTH_USER_MODEL, blank=True)),
                ('topic', models.ForeignKey(to='topic.Topic')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
