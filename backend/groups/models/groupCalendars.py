from django.db import models

from groups.models.groups import Group
# Create your models here.
class Calendar(models.Model):
  group = models.ForeignKey(
    'groups.Group',
    on_delete=models.CASCADE
  )
  start = models.DateTimeField(null=True, blank=True)
  end = models.DateTimeField(null=True, blank=True)
  eventName = models.CharField(max_length=200, default="Meeting")