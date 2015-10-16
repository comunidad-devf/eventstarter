from django.contrib import admin
from events.models import Restriction, Event, EventTier, EventPhoto, \
    EventComment, UserVotesPhoto, UserVotesComment, EventCategory


@admin.register(Restriction)
class RestrictionAdmin(admin.ModelAdmin):
    list_display = ('name',
                    'logo',
                    'created',
                    'modified',)


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('name',
                    'get_image',
                    'start_date',
                    'end_date',
                    'goal',
                    'achieved_goal',
                    'event_completed',
                    'score',)


@admin.register(EventTier)
class EventTierAdmin(admin.ModelAdmin):
    list_display = ('name',
                    'event',
                    'price',
                    'image',
                    'created',
                    'modified',)


@admin.register(EventPhoto)
class EventPhotoAdmin(admin.ModelAdmin):
    list_display = ('user',
                    'event',
                    'image',
                    'positive_votes',
                    'negative_votes',)


@admin.register(EventComment)
class EventCommentAdmin(admin.ModelAdmin):
    list_display = ('user',
                    'event',
                    'positive_votes',
                    'negative_votes',)


@admin.register(UserVotesPhoto)
class UserVotesPhotoAdmin(admin.ModelAdmin):
    list_display = ('user',
                    'positive_vote',
                    'created',
                    'modified',)


@admin.register(UserVotesComment)
class UserVotesCommentAdmin(admin.ModelAdmin):
    list_display = ('user',
                    'positive_vote',
                    'created',
                    'modified',)


@admin.register(EventCategory)
class EventCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',
                    'created',
                    'modified',)
