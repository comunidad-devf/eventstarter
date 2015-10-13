from django.contrib import admin
from event.models import Restriction, Event, Tier, UserFund, EventPhoto, EventComment
# Register your models here.


@admin.register(Restriction)
class RestrictionsAdmin(admin.ModelAdmin):
    list_display = ('name', 'logo', 'description')


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_date', 'end_date', 'due_date', 'goal',
    	            'goal_raised', 'event_realized')
