# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.forms.models import model_to_dict
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from django.http import HttpResponse

from artist_match.models import ArtistProfile, Like, Message
from artist_match.serializers import ArtistCreateSerializer, ArtistReadSerializer
import os
from pprint import pprint
from urlparse import urlparse
from django.http import JsonResponse
# import drogher



class CreateArtist(APIView):

    # def get(self, request, apartment_key='0'):
    #     if (apartment_key == '0'):
    #         packages = Package.objects.filter(status='pending').order_by('date_received')
    #     else:
    #         packages = Package.objects.filter(apartment_no=apartment_key).filter(status='pending').order_by('date_received')
    #         print(packages)
    #
    #     serializer = PackageReadSerializer(packages, many=True)
    #     return Response(serializer.data)

    def post(self, request):
        print(request.data)

        serializer = ArtistCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            print("serialized!")

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            #################### END POST RELATED METHODS ####################




# class Artistl(APIView):
#
#
#     def post(self, request):
#         print(request.data)
#         picked_up = request.data
#         for pack in picked_up:
#             pack_obj = Package.objects.get(id=pack['id'])
#             pack_obj.status = 'picked_up'
#             pack_obj.save()
#         packages = Package.objects.filter(status='pending').order_by('date_received')
#
#         return Response(packages)
#
# class CheckBarcode(APIView):
#
#
#     def post(self, request):
#         print(request.data)
#         package = drogher.barcode('1Z999AA10123456784')
#         print(package.is_valid)
#         print(package.shipper)
#         print(package.tracking_number)
#         a = {
#             'shipper': package.shipper,
#             'tracking': package.tracking_number
#         }
#
#         return Response(a)

class ArtistListView(APIView):
    def get(self, request):
        artists = ArtistProfile.objects.all()
        artists_ser = ArtistReadSerializer(artists, many=True)

        return Response(artists_ser.data)

#
# class ApartmentsListView(APIView):
#
#     def get(self, request):
#         apartments = Apartment.objects.all()
#         for floor in xrange(1,4):
#             print(floor)
#         third_floor = Package.objects.filter(apartment_no__number__startswith='3')
#         third_ser = PackageReadSerializer(third_floor, many=True)
#         packages = {
#             'first_floor' : [],
#             'second_floor' : [],
#             'third_floor' : third_ser.data,
#             'fourth_floor' : []
#         }
#         pprint(packages)
#         for p in third_floor:
#             print(p)
#
#         serializer = ApartmentSerializer(apartments, many=True)
#         return Response(serializer.data)
#
# class ApartmentResidentsView(APIView):
#
#     def get(self, request, apartment_key='0'):
#         if (apartment_key != '0'):
#             apartment = Apartment.objects.get(number=apartment_key)
#             residents = apartment.residents
#         else:
#             return None
#
#         serializer = ResidentSerializer(residents, many=True)
#         return Response(serializer.data)
