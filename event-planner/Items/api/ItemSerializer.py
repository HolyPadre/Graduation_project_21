from rest_framework import serializers

from ..models import Item, images, availability_date, Amenities, ItemType, resevedTable


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = images
        fields = ['item_image']


class Availability_date_Serializer(serializers.ModelSerializer):
    class Meta:
        model = availability_date
        fields = ['availability_time', 'availability_date', 'status']


class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemType
        fields = ['type_name']


class AmenitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Amenities
        fields = ['amenities_name']


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['id','name', 'address', 'location', 'phone', 'link', 'about', 'price',
                  'vendor_id', 'rate', 'types', 'images', 'amenities', 'availability_date','size']
        depth = 1


class ReservedSerializer(serializers.ModelSerializer):
    class Meta:
        model = resevedTable
        fields = ['time']

class updateSerializer(serializers.ModelSerializer):
    class Meta:
        model = resevedTable
        fields = ['status']


class ReserveddSerializer(serializers.ModelSerializer):
    class Meta:
        model = resevedTable
        fields = ['status', 'reserved_date', 'time', 'item', 'event']
        
class ReservedAllSerializer(serializers.ModelSerializer):
    class Meta:
        model = resevedTable
        fields = ['id','status', 'reserved_date', 'time', 'item', 'event']
        depth = 2
        
