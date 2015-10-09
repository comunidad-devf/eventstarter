from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.ForeignKey(User)
    avatar = models.URLField
    bio = models.CharField(max_length=500)
    birth_day = models.DateTimeField()
    phone = models.IntegerField()
    score = models.IntegerField()
    fb_url = models.URLField(null=True)
    twitter_url = models.URLField(null=True)
    fraudulent_user = models.BooleanField(default=False)
