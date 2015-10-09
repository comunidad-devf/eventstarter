from django.contrib import admin
from models import Event, Restrictions, EventPhoto

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'end_date', 'get_organizers', 'city')
