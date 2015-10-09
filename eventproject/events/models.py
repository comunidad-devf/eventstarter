from django.db import models
from person.models import UserProfile


class Restrictions(models.Model):
    name = models.CharField(max_length=50)
    logo = models.ImageField(
        upload_to='static/images/restriction_logo',
        null=True, blank=True)
    description = models.CharField(max_length=1000)


class Event(models.Model):

    """Event Model"""

    name = models.CharField(max_length=100)
    organizers = models.ManyToManyField(UserProfile)
    description = models.CharField(max_length=500)
    requirements = models.CharField(max_length=1000, null=True, blank=True)
    due_date = models.DateField()
    min_attendances = models.IntegerField()
    max_attendances = models.IntegerField()
    restrictions = models.ForeignKey(Restrictions)

    # Place
    place_latitude = models.CharField(max_length=100)
    place_longitude = models.CharField(max_length=100)
    place_name = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    street = models.CharField(max_length=50)
    street_number = models.IntegerField()
    suit_number = models.IntegerField()
    zip_code = models.IntegerField()

    # Funding info
    start_date = models.DateField()
    end_date = models.DateField()
    goal = models.DecimalField(max_digits=10, decimal_places=2)
    goal_currency = models.CharField(max_length=50)
    goal_raised = models.BooleanField(default=False)
    progress = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    # Post event
    event_realized = models.BooleanField(default=False)
    real_attendances = models.IntegerField(default=0)

    # edited
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def get_organizers(self):
        return ' , '.join([x.name for x in self.organizers.all()])


class Tier(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=1000)
    image = models.ImageField(
        upload_to='statics/image/tireimage',
        null=True, blank=True)
    event = models.ForeignKey(Event)


class UserFundsEvent(models.Model):
    event = models.ForeignKey(Event)
    user = models.ForeignKey(UserProfile)
    tier = models.ForeignKey(Tier)
    went = models.BooleanField(default=False)


class EventPhoto(models.Model):
    user = models.ForeignKey(UserProfile)
    event = models.ForeignKey(Event)
    caption = models.ImageField(
        upload_to='static/images/eventphoto',
        null=True, blank=True)
    valid = models.BooleanField(default=True)
    positive_votes = models.IntegerField()
    negative_votes = models.IntegerField()

    def get_logo(self):
        try:
            return
            """<img src="%s"
            style="display: block; width: 40px;"/>""" % self.logo.url
        except:
            return "<h3>No image</h3>"
    get_logo.allow_tags = True


class UserVotesPhoto(models.Model):
    user = models.ForeignKey(UserProfile)
    photo = models.ForeignKey(EventPhoto)
    positive_vote = models.BooleanField(default=False)


class EventComment(models.Model):
    user = models.ForeignKey(UserProfile)
    event = models.ForeignKey(Event)
    comment = models.CharField(max_length=150)


class UserVotesComment(models.Model):
    user = models.ForeignKey(UserProfile)
    comment = models.ForeignKey(EventComment)
    positive_vote = models.BooleanField(default=False)
