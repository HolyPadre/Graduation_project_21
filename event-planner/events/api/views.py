from http import HTTPStatus

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED

from .eventSerializer import EventSerializer, ScheduleSerializer
from ..models import event, event_schdual


@api_view(['GET'])
def ApiOverview(request):
    api_urls = {
        'all_events': '/',
        'Add': '/create',
        'Update': 'update/pk',
        'Delete': '/event/pk/delete',
        'actions/all': 'actions/all',
        'actions/create': 'actions/create'
    }
    return Response(api_urls)


@api_view(['POST'])
def add_event(request):
    event = EventSerializer(data=request.data)
    if event.is_valid():
        event.save()
        return Response(event.data, status=HTTP_201_CREATED)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def add_action(request):
    action = ScheduleSerializer(data=request.data)
    if action.is_valid():
        action.save()
        return Response(action.data, status=HTTP_201_CREATED)



@api_view(['GET'])
def all_actions(request):
    actions = event_schdual.objects.all()
    serializer = ScheduleSerializer(actions, many=True)
    if actions:
        return Response(serializer.data, status=HTTP_200_OK)
    else:
        return Response(serializer.data)


@api_view(['GET'])
def all_events(request):
    # checking for the parameters from the URL
    events = event.objects.all()
    serializer = EventSerializer(events, many=True)

    # if there is something in items else raise error
    if events:
        return Response(serializer.data, status=HTTP_200_OK)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['PUT'])
def update_events(request, pk):
    events = event.objects.get(pk=pk)
    data = EventSerializer(instance=events, data=request.data)

    if data.is_valid():
        data.save()
        return Response(data.data, status=HTTP_201_CREATED)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['DELETE'])
def delete_event(request, pk):
    feed = get_object_or_404(event, pk=pk)
    feed.delete()
    return Response("the event has been deleted",
                    status=status.HTTP_202_ACCEPTED)

