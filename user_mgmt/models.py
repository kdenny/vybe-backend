# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
# from packagemanager.models import Resident

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=25)
    instagram = models.CharField(max_length=100, null=True, blank=True)
    soundcloud = models.CharField(max_length=150, null=True, blank=True)

    def __str__(self):  # __unicode__ for Python 2
        return self.user.username