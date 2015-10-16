# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0007_auto_20151016_1702'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='event_image',
            field=models.ImageField(null=True, upload_to=b'event_media', blank=True),
        ),
    ]
