from __future__ import unicode_literals
from django.db import models
import datetime


class Album(models.Model):
    name = models.CharField(max_length=100, blank=True)
    album_capacity = models.IntegerField(default=501)

    def __unicode__(self):
        return self.name


class Photo(models.Model):
    url_name = models.CharField(max_length=200)
    album = models.ForeignKey(Album, related_name="Photos", blank=False)
    owner = models.CharField(max_length=200)
    like_total = models.IntegerField(blank=True, null=True)
    stored_date = models.DateTimeField(
        default=datetime.datetime.now, null=True
    )

    @staticmethod
    def get_all_photos():
        return Photo.objects.all()

    def __unicode__(self):
        return self.url_name
