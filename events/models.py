"""Events models."""

from django.db import models
from userprofiles.models import UserProfile


class Restriction(models.Model):

    """Restriction model."""

    name = models.CharField(max_length=50)
    logo = models.ImageField(null=True, blank=True, upload_to="event_media")
    description = models.TextField()

    # Meta Data
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        """Return the name, logo, created time and modified time."""
        return "%s %s %s %s" % (self.name,
                                self.logo,
                                self.created,
                                self.modified)


class EventCategory(models.Model):

    """Event Category Model."""

    name = models.CharField(max_length=50)

    # Meta Data
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return "%s" % (self.name)


class Event(models.Model):

    """Event model."""

    organizers = models.ManyToManyField(UserProfile)
    name = models.CharField(max_length=140)
    description = models.TextField()
    requirements = models.TextField(null=True, blank=True)
    restrictions = models.ManyToManyField(Restriction)
    event_image = models.ImageField(upload_to="event_media", null=True, blank=True)
    minimum_attendance = models.IntegerField(default=0)
    maximum_attendance = models.IntegerField(default=0)
    score = models.IntegerField(default=0)
    categories = models.ManyToManyField(EventCategory)

    def get_image(self):
        try:
            return """<img src="{}" style="display: block; width: 60px;"/>""".format(self.event_image.url)
        except:
            return "<h3>No image</h3>"
    get_image.allow_tags = True

    # Date
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    # Due
    due_date = models.DateTimeField()
    goal = models.DecimalField(max_digits=19, decimal_places=2)
    progress = models.DecimalField(max_digits=19, decimal_places=2)

    # Location
    location_name = models.CharField(max_length=255)
    location_latitude = models.CharField(max_length=255, null=True, blank=True)
    location_longitude = models.CharField(max_length=255, null=True, blank=True)
    location_city = models.CharField(max_length=255)
    location_street = models.CharField(max_length=255)
    location_number = models.CharField(max_length=20)
    location_zip_code = models.CharField(max_length=20)
    location_suburb = models.CharField(max_length=255, default=True)#colonia
    location_neighborhood = models.CharField(max_length=255, default=True)# delegacion


    # Finished event data
    attendances = models.IntegerField(default=0)
    achieved_goal = models.BooleanField(default=False)
    event_completed = models.BooleanField(default=False)

    # Meta Data
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return "%s %s %s %s %s %s %s" % (self.name,
                                         self.start_date,
                                         self.end_date,
                                         self.due_date,
                                         self.goal,
                                         self.achieved_goal,
                                         self.event_completed,)


class EventTier(models.Model):

    """Event tier.

    Is the payment package that an organizers offers to the funder
    """

    name = models.CharField(max_length=140)
    event = models.ForeignKey(Event)
    price = models.DecimalField(max_digits=19, decimal_places=2)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True, upload_to="event_media")

    # Meta Data
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return '{} {} {} {} {} {}'.format(self.name,
                                          self.event,
                                          self.price,
                                          self.image,
                                          self.created,
                                          self.modified)


class EventPhoto(models.Model):

    """Event Photo Model.

    Is a photo related to an event
    """

    user = models.ForeignKey(UserProfile)
    event = models.ForeignKey(Event)
    caption = models.CharField(max_length=140, null=True, blank=True)
    image = models.ImageField(upload_to="static/img/event_media")
    positive_votes = models.IntegerField(default=0)
    negative_votes = models.IntegerField(default=0)

    # Meta Data
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.event.name


class EventComment(models.Model):

    """Event Comment Model.

    Is a comment about an event
    """

    user = models.ForeignKey(UserProfile)
    event = models.ForeignKey(Event)
    comment = models.CharField(max_length=250)
    positive_votes = models.IntegerField(default=0)
    negative_votes = models.IntegerField(default=0)

    # Meta Data
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return "%s %s %s %s" % (self.name,
                                self.event,
                                self.positive_vote,
                                self.negative_votes)


class UserVotesPhoto(models.Model):

    """User Vote on Photo.

    Vote entitie when user votes photo
    """

    user = models.ForeignKey(UserProfile)
    photo = models.ForeignKey(EventPhoto)
    positive_vote = models.BooleanField(default=False)

    # Meta Data
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return "%s %s %s %s" % (self.user,
                                self.positive_vote,
                                self.created,
                                self.modified)


class UserVotesComment(models.Model):

    """User Vote on Comment.

    Vote entitie when user votes comment
    """

    user = models.ForeignKey(UserProfile)
    comment = models.ForeignKey(EventComment)
    positive_vote = models.BooleanField(default=False)

    # Meta Data
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return "%s %s %s %s" % (self.user,
                                self.positive_vote,
                                self.created,
                                self.modified)
