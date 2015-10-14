from django.contrib import admin
from models import UserProfile


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'score', 'created', 'fraudulent')
    list_filter = ('score', 'fraudulent',)
    list_display_links = ('user',)
    search_fields = ('user',)
