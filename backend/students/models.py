from django.db import models
from courses.models import Course

class Event(models.Model):
    name = models.CharField(max_length=140)
    start = models.DateTimeField(null=True, blank=True)
    end = models.DateTimeField(null=True, blank=True)

class Student(models.Model):
    name = models.CharField(max_length=140)
    email = models.EmailField(max_length=200)
    password = models.CharField(max_length=100)
    bio = models.CharField(max_length=500)
    location = models.CharField(null=True, max_length=200)
    calendar = models.ManyToManyField(Event, blank=True)
    courses = models.ManyToManyField(Course, blank=True)
    photo = models.ImageField(upload_to='userAvatar')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']