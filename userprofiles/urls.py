"""User Profile URLs."""

from django.conf.urls import include, url

urlpatterns = [
    url(r'^logout/$', 'userprofiles.views.user_logout', name='logout'),
]
