"""Events views."""
from django.shortcuts import render
from userprofiles.models import UserProfile
from django.shortcuts import get_object_or_404
from events.models import Event, EventTier
import random
# from django.http import HttpResponse


def events_home(request):
    """Home View.

    This view renders the main page content and have the main
    task of creating a User Profile entity.
    """
    events = Event.objects.filter(event_completed=False)
    if (len(events) > 6):
        events = random.sample(events, 6)
    else:
        events = random.sample(events, len(events))

    top_score = Event.objects.all().order_by('score')
    if (len(top_score) > 2):
        top_score = top_score[::-1][:2]
    else:
        top_score = top_score[::-1]

    context = {
        'events': events,
        'top_scores': top_score
    }
    # Check if user session has an User Profile entity.
    if request.user.is_authenticated():
        try:
            user_profile = UserProfile.objects.get(user=request.user)
        except UserProfile.DoesNotExist:
            user_profile = UserProfile()
            facebook_user = request.user.social_auth.get(provider='facebook')
            facebook_id = facebook_user.uid
            facebook_access_token = facebook_user.extra_data['access_token']
            picture_url = 'https://graph.facebook.com/%s/picture/?width=500&height=500' % facebook_id
            user_profile.user = request.user
            user_profile.avatar = picture_url
            user_profile.facebook_url = 'https://www.facebook.com/app_scoped_user_id/%s/' % facebook_id
            user_profile.save()
    return render(request, 'events/home.html', context)


def event(request, event):
    """ Event Page.
    This view renders the corresponding event's content, funding
    tiers, etc.
    The commented lines are for testing DB items only
    """

    this_event = get_object_or_404(Event, pk=event)
    this_tier = EventTier.objects.filter(event=this_event)
    context = {
        'event': this_event,
        'tier': this_tier
    }
    return render(request, 'events/event.html', context)
