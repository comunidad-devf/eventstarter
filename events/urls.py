"""Events URLs."""
from django.conf.urls import include, url

urlpatterns = [
    url(r'^events_home$',
        'events.views.events_home',
        name='home'),

    url(
        r'^events/(?P<event>\d+)/$', #checar si es con d o w el id
        'events.views.event',
        name='profile'
    ),
]
