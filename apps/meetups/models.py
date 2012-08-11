from django.db import models
from events.models import Event

__authors__ = "Derek Stegelman"
__date__ = "August 2012"

class MeetUp(models.Model):
    title = models.CharField(max_length=250, blank=True, null=True)
    event = models.ForeignKey(Event, blank=True, null=True)
    location = models.CharField(max_length=250, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
