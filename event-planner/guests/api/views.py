from django.db.models import Q
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from django.conf import settings
from django.core.mail import send_mail

from ..models import Guest
from .GuestSerializer import GuestSerializer
from rest_framework import serializers
from rest_framework import status


@api_view(['POST'])
def add_guests(request):
    guest = GuestSerializer(data=request.data)

    # validating for already existing data
    if Guest.objects.filter(**request.data).exists():
        raise serializers.ValidationError('This data already exists')

    if guest.is_valid():
        guest.save()
        return Response(guest.data, status=status.HTTP_201_CREATED)
    else:
        return Response(guest.data)


@api_view(['GET'])
def view_guests(request):
    # checking for the parameters from the URL
    guests = Guest.objects.all()
    serializer = GuestSerializer(guests, many=True)

    # if there is something in items else raise error
    if guests:
        return Response(serializer.data)
    else:
        return Response(serializer.data)


@api_view(['GET'])
def ViewGuestsByEventId(request, event):
    # checking for the parameters from the URL
    guests = Guest.objects.filter(event=event)
    serializer = GuestSerializer(guests, many=True)

    # if there is something in items else raise error
    if guests:
        return Response(serializer.data)
    else:
        return Response(serializer.data)


@api_view(['POST'])
def update_guests(request, pk):
    guests = Guest.objects.get(pk=pk)
    data = GuestSerializer(instance=guests, data=request.data)

    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['DELETE'])
def delete_guests(request, pk):
    guest = get_object_or_404(Guest, pk=pk)
    guest.delete()
    return Response(status=status.HTTP_202_ACCEPTED)


@api_view(['POST'])
def email(request):
    time = request.GET.get('time')
    location = request.GET.get('location')
    name = request.GET.get('name')
    guest = GuestSerializer(data=request.data)

    subject = 'Palestine Planner'

    if guest.is_valid():
        message = ' hello ' + guest.data.get('name') + \
                  '\n I hope this message finds you well.\n I am Writing to you to invite ' \
                  ' you to my event. This will take place on ' + time + ' at ' + location + '\n I hope to see you there 😄'

        email_from = settings.EMAIL_HOST_USER
        recipient_list = [guest.data.get('email'), ]
        send_mail(subject, message, email_from, recipient_list)
        return Response('redirect to a new page')

# @api_view(['POST'])
# def Score(request):
#     account_sid = 'ACeef9eb389c39696bdbf480a204ef798c'
#     auth_token = 'dafb807ec07584ec9a5ef59f59f972d3'
#     client = Client(account_sid, auth_token)
#
#     message = client.messages.create(
#         body=f'Hi, your test result is . Great job',
#         from_='+15017122661',
#         to='+970569257917',
#     )
#
#     return Response('message send')
