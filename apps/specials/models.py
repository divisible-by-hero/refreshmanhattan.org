from django.db import models


__authors__ = "Derek Stegelman"
__date__ = "August 2012"


class Bar(models.Model):
    name = models.CharField(max_length=250, blank=True, null=True)