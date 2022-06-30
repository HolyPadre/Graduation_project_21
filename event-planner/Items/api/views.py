import os

import pandas as pd
from rest_framework import status, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from ..models import Item, ItemType, resevedTable
from .ItemSerializer import ItemSerializer, TypeSerializer, ReservedSerializer, ReserveddSerializer, \
    ReservedAllSerializer,updateSerializer


@api_view(['GET'])
def all_item_capisty(request):
    type = request.query_params.get('type', None).split(',')

    location = request.GET.getlist('location')
    size = request.GET.get('size')
    print(type)
    print(location)

    items = Item.objects.all().filter(location__in=location, types__in=type, size__gte=size).distinct().order_by(
        '-size')
    serializer = ItemSerializer(items, many=True)

    if items:
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def all_item_Most_rated(request):
    type = request.query_params.get('type', None).split(',')
    location = request.GET.getlist('location')
    print(type)
    print(location)

    items = Item.objects.all().filter(location__in=location, types__in=type).distinct().order_by('-rate')
    serializer = ItemSerializer(items, many=True)

    if items:
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def all_item_by_price_DESC(request):
    type = request.query_params.get('type', None).split(',')
    location = request.GET.getlist('location')
    print(type)
    print(location)

    items = Item.objects.all().filter(location__in=location, types__in=type).distinct().order_by('-price')
    serializer = ItemSerializer(items, many=True)

    if items:
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def all_item_by_price_ASC(request):
    type_ids = request.query_params.get('type', None).split(',')
    location = request.GET.getlist('location')
    print(type)
    print(location)
    items = Item.objects.all().filter(location__in=location, types__in=type_ids).distinct().order_by('price')
    serializer = ItemSerializer(items, many=True)

    if items:
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def returnAvalibleTime(request, pk):
    date = request.GET.get('date')
    reserved = resevedTable.objects.filter(item=pk, reserved_date=date).distinct()
    serializer = ReservedSerializer(reserved, many=True)

    if reserved:
        return Response(serializer.data)
    else:
        return Response(serializer.data)


@api_view(['GET'])
def all_item_has_type(request):
    type_ids = request.query_params.get('id', None).split(',')
    location = request.GET.getlist('location')
    items = Item.objects.all().filter(types__in=type_ids, location__in=location).distinct()
    serializer = ItemSerializer(items, many=True)

    # if there is something in items else raise error
    if items:
        return Response(serializer.data)
    else:
        return Response(serializer.error_messages)


@api_view(['GET'])
def all_item_by_name(request):
    name = request.GET.get('name')
    items = Item.objects.all().filter(name__contains=name).distinct()
    serializer = ItemSerializer(items, many=True)

    # if there is something in items else raise error
    if items:
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def all_item_by_location_and_type(request):
    type = request.GET.getlist('type')
    location = request.GET.getlist('location')
    print(type)
    print(location)

    items = Item.objects.all().filter(location__in=location, types__in=type).distinct()
    serializer = ItemSerializer(items, many=True)

    # if there is something in items else raise error
    if items:
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def all_type(request):
    types = ItemType.objects.all()
    serializer = TypeSerializer(types, many=True)
    if types:
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def all_items(request):
    # checking for the parameters from the URL
    items = Item.objects.all()
    serializer = ItemSerializer(items, many=True)

    # if there is something in items else raise error
    if items:
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def all_requests(request):
    # checking for the parameters from the URL
    items = resevedTable.objects.all()
    serializer = ReservedAllSerializer(items, many=True)

    # if there is something in items else raise error
    if items:
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


class ItemViewSet(viewsets.ModelViewSet):
    serializer_class = ItemSerializer

    def get_queryset(self):
        items = Item.objects.all()
        return items


# @api_view(['GET'])
# class ItemViewSet(viewsets.ModelViewSet):
#     serializer_class = ItemSerializer
#
#     def get_queryset(self):
#         items = Item.objects.all()
#         return items
#
#     def create(self, request, *args, **kwargs):
#         data = request.data
#
#         new_item = Item.objects.create(
#             name=data["name"], address=data['address'], location=data["location"], phone=data["phone"],
#             link=data["link"], about=data["about"], price=data["price"], vendor_id=data["vendor_id"]
#             , reserved=data["reserved"])
#
#         new_item.save()
#
#         for type in data["types"]:
#             types = ItemType.objects.get(type_name=type["type_name"])
#             new_item.types.add(types)
#
#         for amenities in data["types"]:
#             aamenities = ItemType.objects.get(module_name=amenities["amenities_name"])
#             new_item.amenities.add(aamenities)
#
#         for date in data["availability_date"]:
#             dates = ItemType.objects.get(availability_date=date["availability_date"],
#                                          availability_time=date["availability_time"],
#                                          status=date["status"])
#             new_item.availability_date.add(dates)
#
#         for images in data["images"]:
#             imagess = ItemType.objects.get(item_image=images["item_image"])
#             new_item.images.add(imagess)
#
#         serializer = ItemSerializer(new_item)
#
#         return Response(serializer.data)


class ItemViewSet(viewsets.ModelViewSet):
    serializer_class = ItemSerializer

    def get_queryset(self):
        items = Item.objects.all()
        return items


@api_view(['POST'])
def add_request(request):
    requests = ReserveddSerializer(data=request.data)
    if requests.is_valid():
        requests.save()
        return Response(requests.data, status=HTTP_201_CREATED)


def important_features(datasets):
    data = datasets.copy()
    for i in range(0, datasets.shape[0]):
        data["imp"] = data["name"].apply(str) + " " + data["location"].apply(str) + " " + data["price"].apply(
            str) + " " + data["rate"].apply(str) + " " + data["types"].apply(str) + " " + data["amenities"].apply(str)
    return data


@api_view(['GET'])
def all_Recommended_Item(request):
    itemstr = request.GET.get('itemstr')
    csv_filename = os.path.join(os.path.dirname(__file__), 'dataset.csv')

    data = pd.read_csv(csv_filename)
    vec = TfidfVectorizer()

    vecs = vec.fit_transform(data["imp"].apply(lambda x: np.str_(x)))

    vecs.shape

    sim = cosine_similarity(vecs)

    sim.shape

    def recommend(imp):
        venue_id = data[data.name == imp]["ids"].values[0]
        scores = list(enumerate(sim[venue_id]))
        sorted_scores = sorted(scores, key=lambda x: x[1], reverse=True)
        sorted_scores = sorted_scores[0:]
        venues = [data[venues[0] == data["ids"]]["id"].values[0] for venues in sorted_scores]
        return venues

    lst = recommend(itemstr)

    # lst = recommend("Cruise Newport Beach-Yacht Rentals Jericho 30.0 5 id: 2, type_name: Concert, id: 8, type_name: Conference id: 106, amenities_name: Ice chest, id: 459, amenities_name: Selfie Room, id: 477, amenities_name: Many different and flexible space configurations available with our floor plan to accommodate all kinds of events, large and small, outdoor patio with music and lights and inside areas that give us a lot of options., id: 485, amenities_name: Kosher available, id: 615, amenities_name: Worldclass nightlife resources at your disposal., id: 687, amenities_name: HalfBasketball Court")
    lst = lst[1:20]
    items = Item.objects.filter(id__in=lst)
    serializer = ItemSerializer(items, many=True)
    return Response(serializer.data)



@api_view(['PUT'])
def updateAvalibleTime(request, pk):

    reserved = resevedTable.objects.get(pk=pk)
    reserved.status = request.data.get("status")
    print(request.data.get("status"))
    serializer = updateSerializer(instance=reserved, data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.data)
