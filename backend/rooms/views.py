from django.shortcuts import render
from django.http import JsonResponse
from students.serializers import StudentSerializer

from groups.models.groups import Group
from .models import Room, Member
from students.models import Student
# Create your views here.
def index(request, id=id):
  rooms = []
  for room in Room.objects.all():
      rooms.append({
        'name': room.name,
        'id': room.id,
        'description': room.description
      })
  return JsonResponse(rooms, safe=False)

def getRoomById(request, id=id):
  result = {}
  for room in Room.objects.all():
    if room.id == id:
      members = getRoomMember(id)
      result = {
        'name': room.name,
        'id': room.id,
        'description': room.description,
        'members': members
      }
      break
  return JsonResponse(result, safe=False)

def getRoomMember(id):
  roomMembers = []
  for memb in Member.objects.all():
    if (memb.room.id == id):
      info = StudentSerializer(memb.student).data
      roomMembers.append(info)
  return roomMembers
      
def joinRoom(request, id, rid):
  student = getStudent(id)
  for room in Room.objects.all():
    if (room.id == rid):
      room.members.add(student)
  return rid
  

def getStudent(id):
  for student in Student.objects.all():
    if (student.id == id):
      return student
  return null
        