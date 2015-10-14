from django import forms
from events.models import Event


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name',
                  'description',
                  'requirements',
                  'video_url',
                  'minimum_attendance',
                  'maximum_attendance',
                  'start_date',
                  'end_date',
                  'due_date', ]


class AddressForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['location_name']
