from django.db import models
from students.models import Student
from groups.models.groups import Group

# Create your models here.
class GroupMember(models.Model):
  group = models.ForeignKey(
    'groups.Group',
    on_delete=models.RESTRICT
  )
  member = models.ForeignKey(
    'students.Student',
    on_delete=models.RESTRICT
  )
  status = models.BooleanField(default=False)