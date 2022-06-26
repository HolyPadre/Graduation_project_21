from django.db import models

# Create your models here.


from django.db import models

from users.models import User


# Create your models here.
class Contract(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=300, blank=False)
    email = models.CharField(max_length=5000, blank=False)
    status = models.BooleanField(default=False)
    createdTime = models.DateTimeField(auto_now_add=True)
