from django.shortcuts import render
from django.http import JsonResponse
from datetime import datetime
import json

from .models.groups import Group
# from students.models import Student
from groups.models.groupMembers import GroupMember
from groups.models.groupCalendars import Calendar
from rooms.models import Room
from availability import dummyGroups

from students.serializers import StudentSerializer
from groups.serializers import CalendarSerializer

# Create your views here.
def getGroupById(request, id=id):
  result = {}
  for group in Group.objects.all():
    if group.id == id:
      result = getGroupJson(group)
      break
  return JsonResponse(result, safe=False)

def index(request, id=id):
  groups = []
  for group in Group.objects.all():
      # 2019-01-07 10:00
      # startTime = group.preferredmeetingStartTime.strftime("%Y-%m-%d %H:%M")
      # endTime = group.preferredmeetingEndTime.strftime("%Y-%m-%d %H:%M")
      groups.append(getGroupJson(group))
  return JsonResponse(groups, safe=False)

def getPermission(request, gid, zid):
  result = {
    'inGroup': False,
    'isMember': False,
    'isOwner': False
  }
  for groupMem in GroupMember.objects.all():
    if (groupMem.group.id == gid and groupMem.member.id == zid):
      if groupMem.status == True:
        result = {
          'inGroup': True,
          'isMember': True,
          'isOwner': False
        }
      else:
        result = {
          'inGroup': True,
          'isMember': False,
          'isOwner': False
        }
      break
    elif (groupMem.group.id == gid and groupMem.group.owner.id == zid):
      result = {
        'inGroup': True,
        'isMember': True,
        'isOwner': True
      }
      break
  return JsonResponse(result, safe=False)

def getGroupByRoom(request, rid):
  groups = []
  for group in Group.objects.all():
    if group.room.id == rid:
      groups.append(getGroupJson(group))

  return JsonResponse(groups, safe=False)

def getGroupJson(group):
    photo = json.dumps(str(group.photo))
    # 2019-01-07 10:00
    # startTime = group.preferredmeetingStartTime.strftime("%Y-%m-%d %H:%M")
    # endTime = group.preferredmeetingEndTime.strftime("%Y-%m-%d %H:%M")
    id = group.id
    members = getMember(id)
    # skills = getSkills(id)
    vacancy = group.capacity - len(members) - 1
    events = getCalendar(id)
    result = {
      'id': group.id,
      'name': group.name, 
      'room': group.room.name,
      'owner': StudentSerializer(group.owner).data,
      'members': members,
      'descript': group.description,
      'location': group.preferredmeetingLoc,
      'photo': photo,
      'skills': group.skills,
      'capacity': group.capacity,
      'vacancy': vacancy,
      'events': events
    }

    return result

def getMember(id):
  members = []
  for group in Group.objects.all():
    if group.id == id:
      info = StudentSerializer(group.owner).data
      members.append(info)
    
  for groupMem in GroupMember.objects.all():
    if (groupMem.group.id == id and groupMem.status):
      info = StudentSerializer(groupMem.member).data
      members.append(info)

  return members
 
# def getSkills(id):
#   skills = []
#   for gk in GroupSkill.objects.all():
#     if(gk.group.id == id):
#       skills.append(gk.skill.name)
#   return skills

def getCalendar(id):
  events = []
  for event in Calendar.objects.all():
    if event.group.id == id:
      events.append(CalendarSerializer(event).data)
  return events

def addPhoto(request, gid, photo):
  result = {}
  group = Group.objects.get(id=gid)
  group.photo = photo
  group.save()
  return JsonResponse(result, safe=False)

def addDes(request, gid, descrip):
  result = {}
  group = Group.objects.get(id=gid)
  group.description = descrip
  group.save()
  result = {"description" : group.description}
  return JsonResponse(result, safe=False)

def addCalendar(request, gid):
  events = []
  group = Group.objects.get(id=gid)
  dummyEvents = dummyGroups[gid-1]
  for event in dummyEvents["preferredMeetingTimes"]:
        cal = Calendar.objects.create(
          group=group,
          eventName=event["name"],
          start=event["start"],
          end=event["end"]
        )
        cal.save()
        events.append(CalendarSerializer(cal).data)
  return JsonResponse(events, safe=False)

def deleteGroup(request, gid):
  result = {}
  group = Group.objects.get(id=gid)
  for member in GroupMember.objects.all():
        if (member.group == group):
              member.delete()
  group.delete()
  return JsonResponse(result, safe=False)


