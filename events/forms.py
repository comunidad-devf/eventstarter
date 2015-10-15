from django import forms
from events.models import Event, EventCategory, Restriction, EventTier


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name',
                  'video_url',
                  'start_date',
                  'end_date',
                  'due_date',
                  'goal',
                  'description', ]


class AddressForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['location_street',
                  'location_number',
                  'location_suburb',
                  'location_neighborhood',
                  'location_zip_code',
                  'location_city', ]


class AttendancesForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['minimum_attendance',
                  'maximum_attendance', ]


class Category(forms.ModelForm):
    class Meta:
        model = EventCategory
        fields = ['name', ]


class Restrictions(forms.ModelForm):
    class Meta:
        model = Restriction
        fields = ['name',
                  'description', ]


class Tiers(forms.ModelForm):
    class Meta:
        model = EventTier
        fields = ['name',
                  'price',
                  'description', ]
