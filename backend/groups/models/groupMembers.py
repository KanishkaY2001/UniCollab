from django.db import models
from students.models import Student
from groups.models.groups import Group

# Create your models here.
class GroupMember(models.Model):
  group = models.ForeignKey(
    'groups.Group',
    on_delete=models.CASCADE
  )
  member = models.ForeignKey(
    'students.Student',
    on_delete=models.CASCADE
  )
  status = models.BooleanField(default=False)

  skills = models.CharField(max_length=1000, default="")

  # class Meta:
  #   unique_together = ['group', 'member']