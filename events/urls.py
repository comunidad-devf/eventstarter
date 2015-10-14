"""Events URLs."""
from django.conf.urls import include, url

urlpatterns = [
    url(r'^$', 'events.views.events_home', name='home'),
    url(r'^crear_evento/$', 'events.views.create_event', 
    	    name='create_event'),
]
