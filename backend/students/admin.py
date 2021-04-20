from django.contrib import admin

# Register your models here.
from .models import Student, Event

admin.site.register(Student)
admin.site.register(Event)