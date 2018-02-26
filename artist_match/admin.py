# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from artist_match.models import ArtistProfile, Like, Message

# Register your models here.

admin.site.register(ArtistProfile)
admin.site.register(Like)
admin.site.register(Message)