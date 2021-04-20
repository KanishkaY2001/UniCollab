from django.db import models
from students.models import Student

# Create your models here.
class Room(models.Model):
  name = models.CharField(max_length=120, unique=True)
  description = models.CharField(max_length=500, blank=True, null=True)
  members = models.ManyToManyField(Student, through='Member')

  def __str__(self):
        return self.name

class Member(models.Model):
  student = models.ForeignKey(Student, on_delete=models.CASCADE)
  room = models.ForeignKey(Room, on_delete=models.CASCADE)

  class Meta:
    unique_together = ["student", "room"]