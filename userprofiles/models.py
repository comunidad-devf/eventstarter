"""User Profiles model."""

from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):

    """User Profile model."""

    user = models.ForeignKey(User)
    avatar = models.URLField(null=True, blank=True)
    biography = models.TextField(null=True, blank=True)
    birthday = models.DateField(null=True, blank=True)
    phone = models.CharField(max_length=15, null=True, blank=True)
    score = models.IntegerField(default=0)
    credit = models.DecimalField(default=0, max_digits=8, decimal_places=2)
    facebook_url = models.URLField(null=True, blank=True)
    twitter_url = models.URLField(null=True, blank=True)
    fraudulent = models.BooleanField(default=False)

    # Meta Data
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return '{} {} {} {} {} {} {} {} {} {}'.format(self.user,
                                                      self.avatar,
                                                      self.biography,
                                                      self.birthday,
                                                      self.phone,
                                                      self.score,
                                                      self.credit,
                                                      self.facebook_url,
                                                      self.twitter_url,
                                                      self.fraudulent,
                                                      )
