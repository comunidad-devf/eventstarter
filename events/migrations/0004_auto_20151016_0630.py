# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_auto_20151015_1824'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='goal',
            field=models.DecimalField(max_digits=19, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='event',
            name='progress',
            field=models.DecimalField(max_digits=19, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='eventphoto',
            name='image',
            field=models.ImageField(upload_to=b'static/img/event_media'),
        ),
    ]
