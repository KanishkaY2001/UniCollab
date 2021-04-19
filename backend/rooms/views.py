from django.shortcuts import render
from django.http import JsonResponse

from .models import Room, Member
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
      members = getRoom(id)
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
    if (memb.group.id == id and memb.status):
      info = StudentSerializer(memb.member).data
      roomMembers.append(info)
  return roomMembers

def getGrouplessMembers()
  