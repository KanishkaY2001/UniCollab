from django.db import models
from courses.models import Course
from groups.models import Group
from rooms.models import Room, Member
class Student(models.Model):
    name = models.CharField(max_length=140)
    courses = models.ManyToManyField(Course, through='CompletedA')
    rating = models.IntegerField()
    preferredmeetingLoc = models.CharField(max_length=500)
    preferredmeetingStartTime = models.DateTimeField(null=True, blank=True)
    preferredmeetingEndTime = models.DateTimeField(null=True, blank=True)
    photo = models.ImageField(upload_to='groupAvatar')
    rooms = models.ManyToManyField(Room, through='Member')
    class Meta:
        ordering = ['name']
class CompletedA(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)