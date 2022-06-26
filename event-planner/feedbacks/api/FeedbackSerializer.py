from django.db.models import fields
from rest_framework import serializers
from ..models import Feedback


class FeedbackSerializer(serializers.ModelSerializer):
	class Meta:
		model = Feedback
		fields = ('user', 'email', 'description', 'ctime')
