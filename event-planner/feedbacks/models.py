from django.db import models

from users.models import User
# Create your models here.
class Feedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.CharField(max_length=300, blank=False)
    description = models.CharField(max_length=5000, blank=False)
    ctime = models.DateTimeField(auto_now_add=True)

