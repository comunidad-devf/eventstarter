from django.db import models
from user_profile.models import UserProfile


class Restriction(models.Model):
    name = models.CharField(max_length=255)
    logo = models.ImageField(upload_to="logoEvent", null=True, blank=True)
    description = models.CharField(max_length=255)

    def __unicode__(self):
        return '{} {} {}'.format(self.name,
                                 self.logo,
                                 self.description)


class Event(models.Model):
    organizers = models.ManyToManyField(UserProfile)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    image = models.ImageField(upload_to="eventPhoto", null=True, blank=True)
    place_latitude = models.CharField(max_length=255, null=True, blank=True)
    place_longitude = models.CharField(max_length=255, null=True, blank=True)
    reuirements = models.CharField(max_length=255, null=True, blank=True)
    restrictions = models.ManyToManyField(Restriction)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    due_date = models.DateField()
    goal = models.FloatField()
    min_assistants = models.IntegerField()
    max_assistants = models.IntegerField()
    progress = models.DecimalField(max_digits=19, decimal_places=10)
    video = models.URLField(null=True, blank=True)
    goal_raised = models.BooleanField()
    event_realized = models.BooleanField()
    score = models.FloatField()
    city = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    number = models.CharField(max_length=10)
    zip_code = models.CharField(max_length=10)
    place_name = models.CharField(max_length=255, null=True, blank=True)

    def __unicode__(self):
        return '{} {} {} {} {} {} {} {}'.format(self.name,
                                                self.start_date,
                                                self.end_date,
                                                self.due_date,
                                                self.goal,
                                                self.progress,
                                                self.goal_raised,
                                                self.event_realized)

    def get_organizers(self):
        return UserProfile.objects.all()


class Tier(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    price = models.FloatField()
    description = models.CharField(max_length=255)
    tier_image = models.ImageField(upload_to="tierImages", null=True,
                                   blank=True)
    event = models.ForeignKey(Event)

    def __unicode__(self):
        return '{} {} {} {} {}'.format(self.name,
                                       self.price,
                                       self.description,
                                       self.tier_image,
                                       self.event)


class UserFund(models.Model):
    user = models.ForeignKey(UserProfile)
    event = models.ForeignKey(Event)
    tier = models.ForeignKey(Tier)
    went = models.BooleanField()
    created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return '{} {} {} {} {}'.format(self.user,
                                       self.event, self.tier,
                                       self.went)


class EventPhoto(models.Model):
    user = models.ForeignKey(UserProfile)
    event = models.ForeignKey(Event)
    image = models.ImageField(upload_to="uploadedPhotos")
    caption = models.CharField(max_length=255, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    valid = models.BooleanField()

    def __unicode__(self):
        return '{} {} {} {} {} {}'.format(self.user,
                                          self.event,
                                          self.image,
                                          self.caption,
                                          self.created,
                                          self.valid)


class EventComment(models.Model):
    user = models.ForeignKey(UserProfile)
    event = models.ForeignKey(Event)
    comment = models.CharField(max_length=145)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return '{} {} {} {} {}'.format(self.user,
                                       self.event,
                                       self.comment,
                                       self.created,
                                       self.modified)


class PhotoVotes(models.Model):
    positive = models.BooleanField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return '{} {} {}'.format(self.positive,
                                 self.created,
                                 self.modified)


class CommentVotes(models.Model):
    positive = models.BooleanField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return '{} {} {}'.format(self.positive,
                                 self.created,
                                 self.modified)
