# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class ArtistProfile(models.Model):
    name = models.CharField(max_length=150)
    artist_type = models.CharField(max_length=150, default='musician')
    genre = models.CharField(max_length=150, default='')
    city = models.CharField(max_length=150)
    latitude = models.FloatField()
    longitude = models.FloatField()
    soundcloud_id = models.CharField(max_length=25, default='')

        # Returns the string representation of the model.
    def __unicode__(self):              # __unicode__ on Python 2
        return str(self.name)

class Like(models.Model):
    artist_1 = models.ForeignKey(ArtistProfile, related_name='likes')
    artist_2 = models.ForeignKey(ArtistProfile, related_name='liked_you')
    swiped_on = models.DateTimeField(auto_now_add=True)
    liked = models.BooleanField(default=False)
    matched = models.BooleanField(default=False)

        # Returns the string representation of the model.
    def __unicode__(self):              # __unicode__ on Python 2
        return str(self.artist_1) + '-' + str(self.liked_artist)


class Message(models.Model):
    match = models.ForeignKey(Like, related_name='messages')
    sender = models.ForeignKey(ArtistProfile, related_name='sent_messages')
    receiver = models.ForeignKey(ArtistProfile, related_name='received_messages')
    message_text = models.TextField()
    sent_on = models.DateTimeField(auto_now_add=True)
    seen = models.BooleanField(default=False)


        # Returns the string representation of the model.
    def __unicode__(self):              # __unicode__ on Python 2
        return str(self.sender) + '-' + str(self.receiver)



