from django.contrib import admin
from event.models import Restriction, Event, Tier, UserFund, EventPhoto, EventComment
# Register your models here.


@admin.register(Restriction)
class RestrictionsAdmin(admin.ModelAdmin):
    list_display = ('name', 'logo', 'description')


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('get_organizers',)
