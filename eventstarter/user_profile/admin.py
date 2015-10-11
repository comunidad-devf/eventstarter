from django.contrib import admin
from user_profile.models import UserProfile

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
	"""docstring for ProfileUserAdmin"""
	list_display =('user',)

