from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.ForeignKey(User)
    avatar = models.URLField(max_length=255)
    bio = models.CharField(max_length=255, null=True, blank=True)
    birthday = models.DateField()
    phone = models.CharField(max_length=15)
    score = models.FloatField()
    fb_URL = models.URLField(max_length=255, null=True)
    tw_URL = models.URLField(max_length=255, null=True)
    fraudulent_user = models.BooleanField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return '{} {} {} {}'.format(self.user, self.avatar, self.created,
                                    self.modified,)
