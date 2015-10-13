# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofiles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=140)),
                ('description', models.TextField()),
                ('requirements', models.TextField(null=True, blank=True)),
                ('video_url', models.URLField(null=True, blank=True)),
                ('minimum_attendance', models.IntegerField(default=0)),
                ('maximum_attendance', models.IntegerField(default=0)),
                ('score', models.IntegerField(default=0)),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('due_date', models.DateTimeField()),
                ('goal', models.DecimalField(max_digits=19, decimal_places=10)),
                ('progress', models.DecimalField(max_digits=19, decimal_places=10)),
                ('location_name', models.CharField(max_length=255)),
                ('location_latitude', models.CharField(max_length=255, null=True, blank=True)),
                ('location_longitude', models.CharField(max_length=255, null=True, blank=True)),
                ('location_city', models.CharField(max_length=255)),
                ('location_street', models.CharField(max_length=255)),
                ('location_number', models.CharField(max_length=20)),
                ('location_zip_code', models.CharField(max_length=20)),
                ('attendances', models.IntegerField(default=0)),
                ('achieved_goal', models.BooleanField(default=False)),
                ('event_completed', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('organizers', models.ManyToManyField(to='userprofiles.UserProfile')),
            ],
        ),
        migrations.CreateModel(
            name='EventComment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('comment', models.CharField(max_length=250)),
                ('positive_votes', models.IntegerField(default=0)),
                ('negative_votes', models.IntegerField(default=0)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('event', models.ForeignKey(to='events.Event')),
                ('user', models.ForeignKey(to='userprofiles.UserProfile')),
            ],
        ),
        migrations.CreateModel(
            name='EventPhoto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('caption', models.CharField(max_length=140, null=True, blank=True)),
                ('image', models.ImageField(upload_to=b'event_media')),
                ('positive_votes', models.IntegerField(default=0)),
                ('negative_votes', models.IntegerField(default=0)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('event', models.ForeignKey(to='events.Event')),
                ('user', models.ForeignKey(to='userprofiles.UserProfile')),
            ],
        ),
        migrations.CreateModel(
            name='EventTier',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=140)),
                ('price', models.DecimalField(max_digits=19, decimal_places=10)),
                ('description', models.TextField(null=True, blank=True)),
                ('image', models.ImageField(null=True, upload_to=b'event_media', blank=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('event', models.ForeignKey(to='events.Event')),
            ],
        ),
        migrations.CreateModel(
            name='Restriction',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('logo', models.ImageField(null=True, upload_to=b'event_media', blank=True)),
                ('description', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserVotesComment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('positive_vote', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('comment', models.ForeignKey(to='events.EventComment')),
                ('user', models.ForeignKey(to='userprofiles.UserProfile')),
            ],
        ),
        migrations.CreateModel(
            name='UserVotesPhoto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('positive_vote', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('photo', models.ForeignKey(to='events.EventPhoto')),
                ('user', models.ForeignKey(to='userprofiles.UserProfile')),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='restrictions',
            field=models.ManyToManyField(to='events.Restriction'),
        ),
    ]
