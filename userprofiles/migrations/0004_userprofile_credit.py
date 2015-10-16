# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofiles', '0003_auto_20151014_0403'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='credit',
            field=models.DecimalField(default=0, max_digits=8, decimal_places=2),
        ),
    ]
