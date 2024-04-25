from django.db import models
from datetime import datetime
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# # Create your models here.
class Room(models.Model):
    name = models.CharField(max_length=1000)
class Message(models.Model):
    value = models.CharField(max_length=1000000)
    date = models.DateTimeField(default=datetime.now, blank=True)
    user = models.CharField(max_length=1000000)
    room = models.CharField(max_length=1000000)

class CustomUser(AbstractUser):
    friends = models.ManyToManyField('self', related_name='user_friends', blank=True)

    def __str__(self):
        return self.username

# Model for storing friend requests
class FriendRequest(models.Model):
    # Sender of the friend request
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='sent_requests')
    
    # Receiver of the friend request
    receiver = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='received_requests')
    
    # Status of the friend request (pending/accepted/rejected)
    status = models.CharField(max_length=10, choices=[('pending', 'Pending'), ('accepted', 'Accepted'), ('rejected', 'Rejected')])
    
    # Timestamp of when the request was made
    timestamp = models.DateTimeField(auto_now_add=True)

    # String representation of the friend request
    def __str__(self):
        return f"Friend request from {self.sender} to {self.receiver} ({self.status})"

# Model for storing friendships
class Friendship(models.Model):
    # User1 in the friendship
    user1 = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user1_friendships')
    
    # User2 in the friendship
    user2 = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user2_friendships')
    
    # Timestamp of when the friendship was established
    timestamp = models.DateTimeField(auto_now_add=True)

    # String representation of the friendship
    def __str__(self):
        return f"Friendship between {self.user1} and {self.user2}"