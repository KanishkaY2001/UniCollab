from django.db import models

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=140, unique=True)
    info = models.CharField(max_length=10000, default=True, blank=True, null=True)
    class Meta:
        ordering = ['name']

class Skill(models.Model):
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=200)

    class Meta:
        ordering = ['name']
        unique_together = ['course', 'name']