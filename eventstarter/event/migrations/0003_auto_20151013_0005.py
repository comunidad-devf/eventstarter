# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0002_auto_20151012_2356'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='image',
            field=models.ImageField(null=True, upload_to=b'eventPhoto', blank=True),
        ),
        migrations.AlterField(
            model_name='restriction',
            name='logo',
            field=models.ImageField(null=True, upload_to=b'logoEvent', blank=True),
        ),
        migrations.AlterField(
            model_name='tier',
            name='tier_image',
            field=models.ImageField(null=True, upload_to=b'tierImages', blank=True),
        ),
    ]
