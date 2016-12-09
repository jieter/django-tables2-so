from __future__ import unicode_literals

from django.db import models


class Query(models.Model):
    query = models.CharField(max_length=200, verbose_name="query text")
    parent = models.CharField(max_length=200, verbose_name="query parent")
    active = models.BooleanField(verbose_name="currently active")
    date_added = models.DateTimeField(auto_now_add=True)
    date_deactivated = models.DateTimeField(auto_now_add=True)
