"""Events views."""
from django.shortcuts import render, redirect
from userprofiles.models import UserProfile
from django.http import HttpResponse
from events.models import Event, EventCategory, EventTier, Restriction
from django.shortcuts import get_object_or_404
import random


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

    return render(request, 'events/home.html', {})


def create_event(request):
    if request.method == 'POST':
        event_name = request.POST.get('event_name', None)
        video_url = request.POST.get('video_url', None)
        start_date = request.POST.get('start_date', None)
        end_date = request.POST.get('end_date', None)
        due_date = request.POST.get('due_date', None)
        goal = request.POST.get('goal', None)
        progress = request.POST.get('progress', None)
        event_description = request.POST.get('event_description', None)
        location_street = request.POST.get('location_street', None)
        location_number = request.POST.get('location_number', None)
        location_suburb = request.POST.get('location_suburb', None)
        location_neighborhood = request.POST.get('location_neighborhood', None)
        location_zip_code = request.POST.get('location_zip_code', None)
        location_city = request.POST.get('location_city', None)
        minimum_attendance = request.POST.get('minimum_attendance', None)
        maximum_attendance = request.POST.get('maximum_attendance', None)
        category_name = request.POST.get('category_name', None)
        restriction_name = request.POST.get('restriction_name', None)
        restriction_description = request.POST.get('restriction_description', None)
        tier_name = request.POST.get('tier_name', None)
        tier_price = request.POST.get('tier_price', None)
        tier_description = request.POST.get('tier_description', None)
        if (event_name and
            video_url and
            start_date and
            end_date and
            due_date and
            goal and
            progress and
            event_description and
            location_street and
            location_number and
            location_suburb and
            location_neighborhood and
            location_zip_code and
            location_city and
            minimum_attendance and
            maximum_attendance and
            category_name and
            restriction_name and
            restriction_description and
            tier_name and
            tier_price and
            tier_description):
            event = Event()
            event.name = event_name
            event.video_url = video_url
            event.start_date = start_date
            event.end_date = end_date
            event.due_date = due_date
            event.goal = goal
            event.progress = progress
            event.description = event_description
            event.location_street = location_street
            event.location_number = location_number
            event.location_suburb = location_suburb
            event.location_neighborhood = location_neighborhood
            event.location_zip_code = location_zip_code
            event.location_city = location_city
            event.minimum_attendance = minimum_attendance
            event.maximum_attendance = maximum_attendance
            event.save()
            category = EventCategory()
            category.category_name = category_name
            category.save()
            restriction = Restriction()
            restriction.name = restriction_name
            restriction.description = restriction_description
            restriction.save()
            tier = EventTier()
            tier.event = event
            tier.name = tier_name
            tier.price = tier_price
            tier.description = tier_description
            tier.save()
            return redirect('/evento')
    return render(request, 'events/create.html', {})


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
