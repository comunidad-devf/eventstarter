"""User Porfile Views."""

from django.contrib.auth import logout
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect


def user_logout(request):
    """Log out the user session."""
    logout(request)
    return redirect(reverse('events:home'))
