from rest_framework import serializers
from ..models import event, event_schdual


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = event
        fields = ('id','name', 'type', 'location', 'Date', 'user')


class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = event_schdual
        fields = ('action', 'start_time', 'end_time', 'event')
