# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_extensions.db.fields
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('tag', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('created', django_extensions.db.fields.CreationDateTimeField(editable=False, blank=True, default=django.utils.timezone.now)),
                ('updated', django_extensions.db.fields.ModificationDateTimeField(editable=False, blank=True, default=django.utils.timezone.now)),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='replies')),
            ],
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('title', models.CharField(max_length=50)),
                ('slug', django_extensions.db.fields.AutoSlugField(editable=False, blank=True, populate_from='title')),
                ('content', models.TextField(blank=True)),
                ('created', django_extensions.db.fields.CreationDateTimeField(editable=False, blank=True, default=django.utils.timezone.now)),
                ('updated', django_extensions.db.fields.ModificationDateTimeField(editable=False, blank=True, default=django.utils.timezone.now)),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='topics')),
                ('tags', models.ManyToManyField(to='tag.Tag', related_name='topics')),
            ],
        ),
        migrations.AddField(
            model_name='reply',
            name='topic',
            field=models.ForeignKey(to='topic.Topic', related_name='replies'),
        ),
    ]
