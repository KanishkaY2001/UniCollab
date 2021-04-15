from django.db import models
from .models import Student
# Create your models here.
class Room(models.Model):
  name = models.CharField(maxlength=120)
  owner = models.ForeignKey(
    'Student'
  )

