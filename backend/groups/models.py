from django.db import models
from students.models import Student
from rooms.models import Room

from datetime import datetime
# Create your models here.
class Group(models.Model):
  room = models.ForeignKey(
    'rooms.Room', 
    on_delete=models.CASCADE
  )
  owner = models.ForeignKey(
    'students.Student',
    on_delete=models.RESTRICT
  )

  description = models.CharField(max_length=500)
  name = models.CharField(max_length=120)
  preferredmeetingLoc = models.CharField(max_length=500)
  preferredmeetingStartTime = models.DateTimeField(null=True, blank=True)
  preferredmeetingEndTime = models.DateTimeField(null=True, blank=True)
  photo = models.ImageField(upload_to='groupAvatar')