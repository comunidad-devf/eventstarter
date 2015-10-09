from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):

    """Perfil del Usuario"""

    user = models.ForeignKey(User)
    avatar = models.URLField
    bio = models.CharField(max_length=500)
    birth_day = models.DateTimeField()
    phone = models.IntegerField()
    fb_url = models.URLField(null=True)
    twitter_url = models.URLField(null=True)

    # Respect
    score = models.IntegerField()
    fraudulent_user = models.BooleanField(default=False)

    # edited
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
