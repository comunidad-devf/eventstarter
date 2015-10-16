# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_auto_20151014_0134'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='location_neighborhood',
            field=models.CharField(default=True, max_length=255),
        ),
        migrations.AddField(
            model_name='event',
            name='location_suburb',
            field=models.CharField(default=True, max_length=255),
        ),
    ]
