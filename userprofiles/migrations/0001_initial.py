# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('avatar', models.URLField()),
                ('biography', models.TextField(null=True, blank=True)),
                ('birthday', models.DateField()),
                ('phone', models.CharField(max_length=15, null=True, blank=True)),
                ('score', models.IntegerField(default=0)),
                ('facebook_url', models.URLField(null=True, blank=True)),
                ('twitter_url', models.URLField(null=True, blank=True)),
                ('fraudulent', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
