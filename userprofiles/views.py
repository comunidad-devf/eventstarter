"""User Porfile Views."""

from django.contrib.auth import logout
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect


def user_logout(request):
    """Log out the user session."""
    logout(request)
    return redirect(reverse('events:home'))


def user_profile(request, username):
    """User profile view."""
    return render(request, 'userprofiles/profile.html', {})
