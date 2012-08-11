from django.shortcuts import render
from events.models import Event

def home(request):
    events = Event.objects.all()
    context = {'events': events}
    return render(request, "home.html", context)


__author__ = 'Derek Stegelman'
__date__ = '8/11/12'
