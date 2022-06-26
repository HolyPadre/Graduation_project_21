from django.db import models
from django.db.models.signals import post_save
from django.conf import settings
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser
from rest_framework.authtoken.models import Token


# Create your models here.

class User(AbstractUser):
    is_customer = models.BooleanField(default=False)
    is_vendor = models.BooleanField(default=False)
    is_manager = models.BooleanField(default=False)
    vendor_name = models.CharField(max_length=100, null=True)
    phone = models.CharField(max_length=12, null=True, blank=True)
    bank_name = models.CharField(max_length=100, null=True, blank=True)
    bank_number = models.TextField(null=True, blank=True)
    account_type = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.username


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
