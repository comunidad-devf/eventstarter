"""Events URLs."""
from django.conf.urls import include, url

urlpatterns = [
    url(r'^$', 'events.views.events_home', name='home'),
]
