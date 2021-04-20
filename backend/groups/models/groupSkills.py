from django.db import models
from groups.models.groups import Group
from courses.models import Skill
# Create your models here.


class GroupSkill(models.Model):
  group = models.ForeignKey(
    'groups.Group',
    on_delete=models.CASCADE
  )
  skill = models.ForeignKey(
    'courses.Skill',
    on_delete=models.CASCADE
  )

  class Meta:
    unique_together = ['group', 'skill']