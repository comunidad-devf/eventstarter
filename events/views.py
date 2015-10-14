from django.shortcuts import render

def events_home(request):
    return render(request, 'events/home.html', {})
