"""Events URLs."""
from django.conf.urls import include, url

urlpatterns = [
    url(r'^$',
        'events.views.events_home',
        name='home'),

    url(
        r'^events/(?P<event>\d+)/$',
        'events.views.event',
        name='event'
    ),
]
