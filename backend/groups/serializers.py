from rest_framework.serializers import ModelSerializer

from groups.models.groupCalendars import Calendar

class CalendarSerializer(ModelSerializer):
  class Meta:
      model = Calendar
      fields = ['eventName', 'start', 'end']
