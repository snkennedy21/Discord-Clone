from django.db import models
from django.forms import CharField
from django.contrib.auth.models import User

class Room(models.Model):
  name = models.CharField(max_length=100)
  host = models.ForeignKey(User, on_delete=models.CASCADE)
  topic = models.ForeignKey("Topic", related_name="rooms", on_delete=models.SET_NULL, null=True)
  description = models.TextField(max_length=1000, null=True)
  created = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.name

class Topic(models.Model):
  name = models.CharField(max_length=100)

  def __str__(self):
    return self.name

