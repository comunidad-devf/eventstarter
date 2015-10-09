from django.db import models


class Restrictions(models.Model):
    name = models.CharField(max_length=50)
    logo = models.ImageField(upload_to='logo')
    description = models.CharField(max_length=1000)

    def get_logo(self):
        try:
            return """<img src="%s" style="display: block; width: 40px;"/>""" % self.logo.url
        except:
            return "<h3>No image</h3>"
    get_logo.allow_tags = True

class Event(models.Model):
    name = models.CharField(max_length=100)
    organizers = models.ManyToManyField(UserProfile)
    description = models.CharField(max_length=500)
    place_latitude =
    place_longitude =
    place_name = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    street =  models.CharField(max_length=50)
    street_number = models.IntegerField()
    suit_number = models.IntegerField()
    zip_code = models.IntegerField()
    requirements = models.CharField(max_length=1000, null=True, blank=True)
    start_date = models.DateField()
    end_date = models.DateField()
    due_date = models.DateField()
    goal = models.IntegerField()
    goal_currency = models.CharField(max_length=50)
    goal_raised = models.BooleanField(default=False)
    min_attendances = models.IntegerField()
    max_attendances = models.IntegerField()
    progress = models.IntegerField(default=0)
    event_realized = models.BooleanField(default=False)
    restrictions = ForeignKey(Restrictions)
