from django.db import models

__author__ = 'Derek Stegelman'
__date__ = '8/11/12'


class Event(models.Model):
    title = models.CharField(max_length=250, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    start_date = models.DateField()
    start_time = models.TimeField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    end_time = models.TimeField(blank=True, null=True)

    def __unicode__(self):
        return self.title