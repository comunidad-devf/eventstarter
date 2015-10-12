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
                ('avatar', models.URLField(max_length=255)),
                ('bio', models.CharField(max_length=255, null=True, blank=True)),
                ('birthday', models.DateField()),
                ('phone', models.CharField(max_length=15)),
                ('score', models.FloatField()),
                ('fb_URL', models.URLField(max_length=255, null=True)),
                ('tw_URL', models.URLField(max_length=255, null=True)),
                ('fraudulent_user', models.BooleanField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
