from django.db import models

# Create your models here.
from events.models import event
from users.models import User


class Guest(models.Model):
    name = models.CharField(max_length=300, blank=False)
    email = models.CharField(max_length=300, blank=False)
    relation = models.CharField(max_length=600, blank=False)
    event = models.ForeignKey(event,on_delete=models.CASCADE)
