from rest_framework import serializers

from artist_match.models import ArtistProfile

# class PackageReadSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Package
#
#         fields = ('date_received', 'recipient', 'apartment_no', 'package_type', 'status', 'id')
#         depth = 1



class ArtistCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArtistProfile

        fields = ('name', 'artist_type', 'genre', 'city', 'latitude', 'longitude', 'soundcloud_id' )

class ArtistReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArtistProfile

        fields = ('id', 'name', 'artist_type', 'genre', 'city', 'latitude', 'longitude', 'soundcloud_id' )
#
# class ResidentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Resident
#
#         fields = ('name', 'apartment_number', 'packages', )
#
# class ApartmentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Apartment
#         fields = ('number', 'residents', 'packages' )
#         depth = 1