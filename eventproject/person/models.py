from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.ForeignKey(User)
    fb_url = models.URLField(null=True)
    twitter_url = models.URLField(null=True)
