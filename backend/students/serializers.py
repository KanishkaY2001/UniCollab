from rest_framework.serializers import ModelSerializer

from .models import Student, Event

class StudentSerializer(ModelSerializer):
  class Meta:
      model = Student
      fields = ['id', 'name', 'photo', 'bio']

class EventSerializer(ModelSerializer):
  class Meta:
    model = Event
    fields = ['name', 'start', 'end']