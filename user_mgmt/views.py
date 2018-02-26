# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

# -*- coding: utf-8 -*-

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from .serializers import UserProfileSerializer, JustUserSerializer
from .models import UserProfile, User

# Create your views here.

from rest_framework.response import Response


class Username(APIView):
    def get(self, request):
        current_user = request.user.username

        uu = User.objects.get(username=current_user)

        rp = UserProfile.objects.get(user=uu.id)
        rs = UserProfileSerializer(rp)

        data = {
            'resident': rs.data
        }

        return Response(data)