from django.shortcuts import render
from django.http import JsonResponse
from students.serializers import StudentSerializer
from groups.serializers import CalendarSerializer


from groups.models.groups import Group
from groups.models.groupMembers import GroupMember
from .models import Room, Member
from students.models import Student
from meeting import sortGroupByDistance
from groups.models.groupCalendars import Calendar
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
  student = Student.objects.get(id=id)
  for room in Room.objects.all():
    if (room.id == rid):
      room.members.add(student)
  return rid
  

def getStudentLocJson(id):
  student = Student.objects.get(id=id)
  student = {
    "location" : student.location
  }
  return student

def createGroup(request, id, rid, name):
  groupRet = {}
  student = Student.objects.get(id=id)
  room = Room.objects.get(id=rid)
  group = Group.objects.create(
    room=room,
    owner=student,
    name=name,
    preferredmeetingLoc=student.location
  )
  group.save()
  groupRet = { "id" : group.id }
  return JsonResponse(groupRet, safe=False)

def getLocation(request, id, rid):
  groups = []
  student = getStudentLocJson(id)
  for group in Group.objects.all():
    if group.room.id == rid:
      groups.append(getGroupJson(group))
  sortedGroups = sortGroupByDistance(groups, student)
  return JsonResponse(sortedGroups, safe=False)

def getGroupJson(group):
    photo = json.dumps(str(group.photo))
    id = group.id
    members = getMember(id)
    vacancy = group.capacity - len(members) - 1
    result = {
      'id': group.id,
      'name': group.name, 
      'members': members,
      'descript': group.description,
      'location' : group.preferredmeetingLoc,
      'photo': photo,
      'skills': group.skills,
      'capacity': group.capacity,
      'vacancy': vacancy
    }

    return result
  
def getMember(id):
  members = []
  for group in Group.objects.all():
    if group.id == id:
      info = {
        "name" : group.owner.name
      }
      members.append(info)
  for groupMem in GroupMember.objects.all():
    if (groupMem.group.id == id and groupMem.status):
      info = {
        "name" : groupMem.member.name
      }
      members.append(info)
  return members