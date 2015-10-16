# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_auto_20151015_1824'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='video_url',
        ),
        migrations.AddField(
            model_name='event',
            name='event_image',
            field=models.ImageField(null=True, upload_to=b'event_image', blank=True),
        ),
    ]
