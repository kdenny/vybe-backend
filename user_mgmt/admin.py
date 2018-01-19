# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from user_mgmt.models import UserProfile

# Register your models here.

admin.site.register(UserProfile)