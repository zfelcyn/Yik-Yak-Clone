from django.db import models
from datetime import datetime
from django.contrib.auth.models import AbstractUser

# # Create your models here.
class Room(models.Model):
    name = models.CharField(max_length=1000)
class DirectMessageRoom(models.Model):
    name=models.CharField(max_length=1000)
class Message(models.Model):
    value = models.CharField(max_length=1000000)
    date = models.DateTimeField(default=datetime.now, blank=True)
    user = models.CharField(max_length=1000000)
    room = models.CharField(max_length=1000000)
class User(models.Model):
    name=models.CharField(max_length=1000)
class DirectMessage(models.Model):
    otherUser=models.CharField(max_length=1000)
    value = models.CharField(max_length=1000000)
    date = models.DateTimeField(default=datetime.now, blank=True)
    user = models.CharField(max_length=1000000)

class CustomUser(AbstractUser):
    pass