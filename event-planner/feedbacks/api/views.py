from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from .FeedbackSerializer import FeedbackSerializer
from rest_framework import status
from ..models import Feedback


@api_view(['GET'])
def ApiOverview(request):
    api_urls = {
        'all_feedbacks': '/',
        'Add': '/create',
        'Update': '/update/pk',
        'Delete': '/feedback/pk/delete'
    }
    return Response(api_urls)


@api_view(['POST'])
def add_feedbacks(request):
    feed = FeedbackSerializer(data=request.data)
    if feed.is_valid():
        feed.save()
        return Response(feed.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def all_feedbacks(request):
    # checking for the parameters from the URL
    feeds = Feedback.objects.all()
    serializer = FeedbackSerializer(feeds, many=True)

    # if there is something in items else raise error
    if feeds:
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


def update_feedbacks(request, pk):
    feed = Feedback.objects.get(pk=pk)
    data = FeedbackSerializer(instance=feed, data=request.data)

    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)



@api_view(['DELETE'])
def delete_feedbacks(request, pk):
    feed = get_object_or_404(Feedback, pk=pk)
    feed.delete()
    return Response(
        status=status.HTTP_202_ACCEPTED)