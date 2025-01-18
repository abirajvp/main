from django.db import models
from django.utils import timezone

# Create your models here.
class UserData(models.Model):
    username = models.CharField(max_length=32)
    email = models.EmailField()
    contact = models.CharField(max_length=16)
    password = models.CharField(max_length=64)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class CallLog(models.Model):
    log = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

class NotifiLog(models.Model):
    log = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

class TextLog(models.Model):
    log = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

class Log(models.Model):
    log = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
