"""Events views."""
from django.shortcuts import render
from userprofiles.models import UserProfile
from django.http import HttpResponse
from forms import EventForm, AddressForm


def events_home(request):
    """Home View.

    This view renders the main page content and have the main
    task of creating a User Profile entity.
    """
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
    form = EventForm
    address = AddressForm
    return render(request, 'events/create.html', {
                           'eventform': form,
                           'addressForm': address})
