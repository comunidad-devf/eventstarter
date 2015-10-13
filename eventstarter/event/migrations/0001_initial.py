# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommentVotes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('positive', models.BooleanField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to=b'eventPhoto')),
                ('place_latitude', models.CharField(max_length=255, null=True, blank=True)),
                ('place_longitude', models.CharField(max_length=255, null=True, blank=True)),
                ('reuirements', models.CharField(max_length=255, null=True, blank=True)),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('due_date', models.DateField()),
                ('goal', models.FloatField()),
                ('min_assistants', models.IntegerField()),
                ('max_assistants', models.IntegerField()),
                ('progress', models.DecimalField(max_digits=19, decimal_places=10)),
                ('video', models.URLField(null=True, blank=True)),
                ('goal_raised', models.BooleanField()),
                ('event_realized', models.BooleanField()),
                ('score', models.FloatField()),
                ('city', models.CharField(max_length=255)),
                ('street', models.CharField(max_length=255)),
                ('number', models.CharField(max_length=10)),
                ('zip_code', models.CharField(max_length=10)),
                ('place_name', models.CharField(max_length=255, null=True, blank=True)),
                ('organizers', models.ManyToManyField(to='user_profile.UserProfile')),
            ],
        ),
        migrations.CreateModel(
            name='EventComment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('comment', models.CharField(max_length=145)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('event', models.ForeignKey(to='event.Event')),
                ('user', models.ForeignKey(to='user_profile.UserProfile')),
            ],
        ),
        migrations.CreateModel(
            name='EventPhoto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(upload_to=b'uploadedPhotos')),
                ('caption', models.CharField(max_length=255, null=True, blank=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('valid', models.BooleanField()),
                ('event', models.ForeignKey(to='event.Event')),
                ('user', models.ForeignKey(to='user_profile.UserProfile')),
            ],
        ),
        migrations.CreateModel(
            name='PhotoVotes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('positive', models.BooleanField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Restrictions',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('logo', models.ImageField(null=True, upload_to=b'logoEvent')),
                ('description', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Tier',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, null=True, blank=True)),
                ('price', models.FloatField()),
                ('description', models.CharField(max_length=255)),
                ('tier_image', models.ImageField(null=True, upload_to=b'tierImages')),
                ('event', models.ForeignKey(to='event.Event')),
            ],
        ),
        migrations.CreateModel(
            name='UserFund',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('went', models.BooleanField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('event', models.ForeignKey(to='event.Event')),
                ('tier', models.ForeignKey(to='event.Tier')),
                ('user', models.ForeignKey(to='user_profile.UserProfile')),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='restrictions',
            field=models.ManyToManyField(to='event.Restrictions'),
        ),
    ]
