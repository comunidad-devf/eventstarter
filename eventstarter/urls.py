from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from eventstarter import settings

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url('', include('social.apps.django_app.urls', namespace='social')),
    url('', include('events.urls', namespace='events')),
    url('', include('userprofiles.urls', namespace='userprofiles')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
