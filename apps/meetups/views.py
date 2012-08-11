from django.views.generic import ListView, DetailView

__authors__ = "Derek Stegelman"
__date__ = "August 2012"


class MeetUpListView(ListView):
    context_object_name = "meetups"

class MeetUpDetailView(DetailView):
    context_object_name = "meetup"